#Codeflix_Botz
#rohit_1888 on Tg

import motor, asyncio
import motor.motor_asyncio
import time
import pymongo, os
from config import DB_URI, DB_NAME
import logging
from datetime import datetime, timedelta

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

logging.basicConfig(level=logging.INFO)

default_verify = {
    'is_verified': False,
    'verified_time': 0,
    'verify_token': "",
    'link': ""
}

def new_user(id):
    return {
        '_id': id,
        'verify_status': {
            'is_verified': False,
            'verified_time': "",
            'verify_token': "",
            'link': ""
        }
    }

class Rohit:

    def __init__(self, DB_URI, DB_NAME):
        self.dbclient = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
        self.database = self.dbclient[DB_NAME]

        self.channel_data = self.database['channels']
        self.admins_data = self.database['admins']
        self.user_data = self.database['users']
        self.sex_data = self.database['sex']
        self.banned_user_data = self.database['banned_user']
        self.autho_user_data = self.database['autho_user']
        self.del_timer_data = self.database['del_timer']
        self.fsub_data = self.database['fsub']   
        self.rqst_fsub_data = self.database['request_forcesub']
        self.rqst_fsub_Channel_data = self.database['request_forcesub_channel']

        # NEW COLLECTION FOR SHORTNER + VERIFY EXPIRY
        self.shortner_data = self.database['shortner_settings']


    # ============================
    # USERS
    # ============================

    async def present_user(self, user_id: int):
        found = await self.user_data.find_one({'_id': user_id})
        return bool(found)

    async def add_user(self, user_id: int):
        await self.user_data.insert_one({'_id': user_id})
        return

    async def full_userbase(self):
        user_docs = await self.user_data.find().to_list(length=None)
        user_ids = [doc['_id'] for doc in user_docs]
        return user_ids

    async def del_user(self, user_id: int):
        await self.user_data.delete_one({'_id': user_id})
        return


    # ============================
    # ADMIN
    # ============================

    async def admin_exist(self, admin_id: int):
        found = await self.admins_data.find_one({'_id': admin_id})
        return bool(found)

    async def add_admin(self, admin_id: int):
        if not await self.admin_exist(admin_id):
            await self.admins_data.insert_one({'_id': admin_id})

    async def del_admin(self, admin_id: int):
        if await self.admin_exist(admin_id):
            await self.admins_data.delete_one({'_id': admin_id})

    async def get_all_admins(self):
        admins = await self.admins_data.find().to_list(length=None)
        return [x['_id'] for x in admins]


    # ============================
    # BAN USER
    # ============================

    async def ban_user_exist(self, user_id: int):
        return bool(await self.banned_user_data.find_one({'_id': user_id}))

    async def add_ban_user(self, user_id: int):
        if not await self.ban_user_exist(user_id):
            await self.banned_user_data.insert_one({'_id': user_id})

    async def del_ban_user(self, user_id: int):
        if await self.ban_user_exist(user_id):
            await self.banned_user_data.delete_one({'_id': user_id})

    async def get_ban_users(self):
        bans = await self.banned_user_data.find().to_list(length=None)
        return [x['_id'] for x in bans]


    # ============================
    # DELETE TIMER
    # ============================

    async def set_del_timer(self, value: int):
        existing = await self.del_timer_data.find_one({})
        if existing:
            await self.del_timer_data.update_one({}, {'$set': {'value': value}})
        else:
            await self.del_timer_data.insert_one({'value': value})

    async def get_del_timer(self):
        data = await self.del_timer_data.find_one({})
        return data.get('value', 600) if data else 0


    # ============================
    # CHANNEL MANAGEMENT
    # ============================

    async def channel_exist(self, channel_id: int):
        return bool(await self.fsub_data.find_one({'_id': channel_id}))

    async def add_channel(self, channel_id: int):
        if not await self.channel_exist(channel_id):
            await self.fsub_data.insert_one({'_id': channel_id})

    async def rem_channel(self, channel_id: int):
        if await self.channel_exist(channel_id):
            await self.fsub_data.delete_one({'_id': channel_id})

    async def show_channels(self):
        ch = await self.fsub_data.find().to_list(length=None)
        return [x['_id'] for x in ch]


    # ============================
    # REQUEST FORCE SUB
    # ============================

    async def req_user(self, channel_id: int, user_id: int):
        await self.rqst_fsub_Channel_data.update_one(
            {"_id": channel_id},
            {"$addToSet": {"user_ids": user_id}},
            upsert=True
        )

    async def del_req_user(self, channel_id: int, user_id: int):
        await self.rqst_fsub_Channel_data.update_one(
            {"_id": channel_id},
            {"$pull": {"user_ids": user_id}},
        )

    async def req_user_exist(self, channel_id: int, user_id: int):
        return bool(await self.rqst_fsub_Channel_data.find_one(
            {"_id": channel_id, "user_ids": user_id}
        ))


    # ============================
    # VERIFICATION SYSTEM
    # ============================

    async def db_verify_status(self, user_id):
        user = await self.user_data.find_one({'_id': user_id})
        return user.get('verify_status', default_verify) if user else default_verify

    async def db_update_verify_status(self, user_id, verify):
        await self.user_data.update_one({'_id': user_id}, {'$set': {'verify_status': verify}})

    async def update_verify_status(self, user_id, verify_token="", is_verified=False, verified_time=0, link=""):
        current = await self.db_verify_status(user_id)
        current["verify_token"] = verify_token
        current["is_verified"] = is_verified
        current["verified_time"] = verified_time
        current["link"] = link
        await self.db_update_verify_status(user_id, current)

    async def set_verify_count(self, user_id: int, count: int):
        await self.sex_data.update_one({"_id": user_id}, {"$set": {"verify_count": count}}, upsert=True)

    async def get_verify_count(self, user_id: int):
        data = await self.sex_data.find_one({"_id": user_id})
        return data.get("verify_count", 0) if data else 0


    # ============================
    # SHORTNER SETTINGS + VERIFY EXPIRY
    # ============================

    async def get_shortner_settings(self):
        data = await self.shortner_data.find_one({"_id": "config"})
        if not data:
            return {
                "shortner_enabled": True,
                "short_url": None,
                "short_api": None,
                "tutorial_link": None,
                "verify_expiry": None
            }
        data.pop("_id", None)
        return data

    async def set_shortner_status(self, enabled: bool):
        await self.shortner_data.update_one(
            {"_id": "config"},
            {"$set": {"shortner_enabled": enabled}},
            upsert=True
        )

    async def update_shortner_setting(self, key, value):
        await self.shortner_data.update_one(
            {"_id": "config"},
            {"$set": {key: value}},
            upsert=True
        )

    async def update_verify_expiry_global(self, seconds):
        await self.shortner_data.update_one(
            {"_id": "config"},
            {"$set": {"verify_expiry": seconds}},
            upsert=True
        )

    async def get_verify_expiry_global(self):
        data = await self.shortner_data.find_one({"_id": "config"})
        return data.get("verify_expiry", None) if data else None


db = Rohit(DB_URI, DB_NAME)
