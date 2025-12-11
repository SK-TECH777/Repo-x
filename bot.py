# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

from aiohttp import web
from plugins import web_server
import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
import pytz
from datetime import datetime
# rohit_1888 on Tg
from config import *
from database.db_premium import *
from database.database import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

# Suppress APScheduler logs below WARNING level
logging.getLogger("apscheduler").setLevel(logging.WARNING)

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")

# schedule jobs that depend on db functions (ensure functions exist)
try:
    scheduler.add_job(remove_expired_users, "interval", seconds=10)
except Exception:
    # remove_expired_users might be defined elsewhere or not available
    pass

# Reset verify count for all users daily at 00:00 IST
async def daily_reset_task():
    try:
        await db.reset_all_verify_counts()
    except Exception:
        pass

try:
    scheduler.add_job(daily_reset_task, "cron", hour=0, minute=0)
except Exception:
    pass

name = """
 BY spk_links
"""

def get_indian_time():
    """Returns the current time in IST."""
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

        # default runtime placeholders (will be overwritten from DB if available)
        self.mongodb = None
        self.shortner_enabled = True
        self.short_url = SHORTLINK_URL if 'SHORTLINK_URL' in globals() else None
        self.short_api = SHORTLINK_API if 'SHORTLINK_API' in globals() else None
        self.tutorial_link = TUT_VID if 'TUT_VID' in globals() else None
        self.verify_expiry = VERIFY_EXPIRE if 'VERIFY_EXPIRE' in globals() else None

    async def start(self):
        await super().start()
        # start scheduler after pyrogram loop is ready
        try:
            scheduler.start()
        except Exception:
            pass

        usr_bot_me = await self.get_me()
        self.uptime = get_indian_time()

        # Validate DB channel presence (original behaviour)
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            # test sending (attempt delete to check admin rights)
            try:
                test = await self.send_message(chat_id=db_channel.id, text="Test Message")
                await test.delete()
            except Exception:
                # if test fails, don't exit here — log warning and continue
                self.LOGGER(__name__).warning("Unable to send/delete test message in DB channel. Check bot admin rights.")
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Sk_Anime_1")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Minato_Sencie")
        self.LOGGER(__name__).info("""
  |_| |___/
""")

        self.set_parse_mode(ParseMode.HTML)
        self.username = usr_bot_me.username
        self.LOGGER(__name__).info(f"Bot Running..! Made by https://t.me/Minato_Sencie")

        # ===============================
        #  Load DB + Shortner Settings + Verify Expiry
        # ===============================
        try:
            # Prefer existing global db object if available (from database.database import *)
            try:
                # If `db` was imported by `from database.database import *`
                if 'db' in globals() and db is not None:
                    self.mongodb = db
                else:
                    # fallback: try to import db explicitly
                    from database.database import db as _db
                    self.mongodb = _db
            except Exception:
                # final fallback: try to create a new Rohit instance (unlikely needed)
                try:
                    from database.database import Rohit
                    self.mongodb = Rohit(DB_URI, DB_NAME)
                except Exception:
                    self.mongodb = None

            if self.mongodb:
                # Load shortner settings (single document _id: 'config')
                try:
                    s = await self.mongodb.get_shortner_settings()
                    # fill runtime fields (use config fallbacks if DB values absent)
                    self.shortner_enabled = s.get('shortner_enabled', True)
                    self.short_url = s.get('short_url') or (SHORTLINK_URL if 'SHORTLINK_URL' in globals() else None)
                    self.short_api = s.get('short_api') or (SHORTLINK_API if 'SHORTLINK_API' in globals() else None)
                    self.tutorial_link = s.get('tutorial_link') or (TUT_VID if 'TUT_VID' in globals() else None)
                except Exception as e:
                    self.LOGGER(__name__).warning(f"Failed to load shortner settings from DB: {e}")
                    self.shortner_enabled = True
                    self.short_url = SHORTLINK_URL if 'SHORTLINK_URL' in globals() else None
                    self.short_api = SHORTLINK_API if 'SHORTLINK_API' in globals() else None
                    self.tutorial_link = TUT_VID if 'TUT_VID' in globals() else None

                # Load verify expiry (global override)
                try:
                    ve = await self.mongodb.get_verify_expiry_global()
                    # If DB returns None => use config VERIFY_EXPIRE, else use DB value (can be 0 or int)
                    self.verify_expiry = ve if ve is not None else (VERIFY_EXPIRE if 'VERIFY_EXPIRE' in globals() else None)
                except Exception as e:
                    self.LOGGER(__name__).warning(f"Failed to load verify expiry from DB: {e}")
                    self.verify_expiry = VERIFY_EXPIRE if 'VERIFY_EXPIRE' in globals() else None
            else:
                # No DB attached: use config defaults
                self.mongodb = None
                self.shortner_enabled = True
                self.short_url = SHORTLINK_URL if 'SHORTLINK_URL' in globals() else None
                self.short_api = SHORTLINK_API if 'SHORTLINK_API' in globals() else None
                self.tutorial_link = TUT_VID if 'TUT_VID' in globals() else None
                self.verify_expiry = VERIFY_EXPIRE if 'VERIFY_EXPIRE' in globals() else None

        except Exception as e:
            # Should not crash startup for DB errors; log and continue with config defaults
            self.LOGGER(__name__).warning(f"Unexpected error loading DB settings: {e}")
            self.mongodb = None
            self.shortner_enabled = True
            self.short_url = SHORTLINK_URL if 'SHORTLINK_URL' in globals() else None
            self.short_api = SHORTLINK_API if 'SHORTLINK_API' in globals() else None
            self.tutorial_link = TUT_VID if 'TUT_VID' in globals() else None
            self.verify_expiry = VERIFY_EXPIRE if 'VERIFY_EXPIRE' in globals() else None

        # ===============================

        # Start Web Server (preserve original behavior)
        try:
            app_runner = web.AppRunner(await web_server())
            await app_runner.setup()
            site = web.TCPSite(app_runner, "0.0.0.0", PORT)
            await site.start()
        except Exception as e:
            self.LOGGER(__name__).warning(f"Failed to start web server: {e}")

        # Notify owner that bot started (best-effort)
        try:
            await self.send_message(OWNER_ID, text=f"<b>›› ʜᴇʏ sᴇɴᴘᴀɪ!! \nɪ'ᴍ ᴀʟɪᴠᴇ ɴᴏᴡ 🍃...</b>")
        except Exception:
            pass

    async def stop(self, *args):
        # gracefully stop scheduler
        try:
            scheduler.shutdown(wait=False)
        except Exception:
            pass
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    def run(self):
        """Run the bot."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())
        self.LOGGER(__name__).info("Bot is now running. Thanks to https://t.me/Minato_Sencie")
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            self.LOGGER(__name__).info("Shutting down...")
        finally:
            loop.run_until_complete(self.stop())


#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#
