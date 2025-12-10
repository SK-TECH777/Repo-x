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

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8543127653:AAF4QaA1h_3vv8yqbS24xgzPjq7TLLFbgXo")
APP_ID = int(os.environ.get("APP_ID", "22128383")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7992b5c5c9c6d34276c3dce9e46ba879") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003494765620")) #Your db channel Id
OWNER = os.environ.get("OWNER", "Minato_Sencie") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "5960133511")) # Owner id
ADMINS = [5960133511] # Admin IDs
#--------------------------------------------
PORT = os.environ.get("PORT", "8080")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sktech07:sktech07@cluster0.0mmptus.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "SkAnime")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "600"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/+NLK4xk9F_YYzM2I1")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/pc7mr8.png")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://files.catbox.moe/dpk0pi.jpg")

#--------------------------------------------
# Enable or Disable Verify Mode
VERIFY_MODE = os.environ.get("VERIFY_MODE", "True").lower() == "true"
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "vplink.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "8a97662a9011593aca4eba9e00a5b93b5267b21c")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","https://t.me/Naruto_backup_1/9")

#--------------------------------------------

#--------------------------------------------
HELP_TXT = """
<b><blockquote>
⚙️ <b>ᴛʜɪs ɪs ᴀ ᴀᴅᴠᴀɴᴄᴇ ғɪʟᴇ sʜᴀʀɪɴɢ ʙᴏᴛ:-</b>

❏ <b>ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs</b>
├ /start — sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
├ /myplan — ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
├ /commands — ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴛʜᴇ ʙᴏᴛ (ᴀᴅᴍɪɴ)

💡 <b>ʜᴏᴡ ᴛᴏ ᴜsᴇ:</b>  
1️⃣ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴏᴛ ʟɪɴᴋ  
2️⃣ ᴊᴏɪɴ ᴀʟʟ ʀᴇQᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs  
3️⃣ ᴛʀʏ ᴀɢᴀɪɴ — ᴛʜᴀᴛ’s ɪᴛ ✅

👨‍💻 <b>ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ:</b> <a href='https://t.me/Minato_Sencie'>⏤͟͞ 𝙈𝙞𝙣𝙖𝙩𝙤ˢᵉⁿᶜᶦᵉ</a>
</blockquote></b>
"""

ABOUT_TXT = "<b>›› ғᴏʀ ᴍᴏʀᴇ: <a href='https://t.me/+AdcXPREPNEpkZmNl'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n <blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/+AdcXPREPNEpkZmNl'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @Minato_Sencie\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Minato_Sencie'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> </b></blockquote>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>›› ʜᴇʏ!!, {mention} ~ <blockquote>ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><blockquote>›› ʜᴇʏ × {mention}</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>")
CMD_TXT = """<blockquote><b>›› ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ:</b></blockquote>

<blockquote><b>🚀 ɢᴇɴᴇʀᴀʟ</b></blockquote>

<b>›› /start :</b> ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴏʀ ɢᴇᴛ ᴘᴏꜱᴛꜱ  
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ꜱᴛᴀᴛᴜꜱ  
<b>›› /commands :</b> ᴠɪᴇᴡ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ  

<blockquote><b>🔗 ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛɪᴏɴ</b></blockquote>

<b>›› /batch :</b> ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ꜰᴏʀ ᴍᴏʀᴇ ᴛʜᴀɴ ᴏɴᴇ ᴘᴏꜱᴛꜱ  
<b>›› /custom_batch :</b> ᴄʀᴇᴀᴛᴇ ᴄᴜꜱᴛᴏᴍ ʙᴀᴛᴄʜ ꜰʀᴏᴍ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ  
<b>›› /genlink :</b> ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ꜰᴏʀ ᴏɴᴇ ᴘᴏꜱᴛ  

<blockquote><b>📊 ʙᴏᴛ ꜱᴛᴀᴛɪꜱᴛɪᴄꜱ</b></blockquote>

<b>›› /users :</b> ᴠɪᴇᴡ ʙᴏᴛ ꜱᴛᴀᴛɪꜱᴛɪᴄꜱ 
<b>›› /stats :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ 
<b>›› /count :</b> ᴄᴏᴜɴᴛ ꜱʜᴏʀᴛɴᴇʀ ᴄʟɪᴄᴋꜱ  

<blockquote><b>📢 ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴍᴀɴᴅꜱ</b></blockquote>

<b>›› /broadcast :</b> ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ ʙᴏᴛ ᴜꜱᴇʀꜱ  
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪᴛʜ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ   
<b>›› /pbroadcast :</b> ᴘɪɴ ᴀ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀ'ꜱ ᴄʜᴀᴛ  

<blockquote><b>⏳ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ</b></blockquote>

<b>›› /dlt_time :</b> ꜱᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ ꜰᴏʀ ꜰɪʟᴇꜱ 
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ ꜱᴇᴛᴛɪɴɢ  

<blockquote><b>🚫 ᴜꜱᴇʀ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</b></blockquote>

<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴜꜱɪɴɢ ᴛʜᴇ ʙᴏᴛ  
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴘʀᴇᴠɪᴏᴜꜱʟʏ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀ   
<b>›› /banlist :</b> ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀꜱ  
<b>›› /delreq :</b> ʀᴇᴍᴏᴠᴇ ᴜꜱᴇʀꜱ ᴛʜᴀᴛ ʟᴇꜰᴛ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɴᴏᴛ ɢᴇᴛᴛɪɴɢ ʀᴇQᴜᴇꜱᴛ ꜰꜱᴜʙ  

<blockquote><b>📺 ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ</b></blockquote>

<b>›› /addchnl :</b> ᴀᴅᴅ ᴀ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ  
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ᴀ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ  
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀʟʟ ᴀᴅᴅᴇᴅ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟꜱ 
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴏɴ ᴏʀ ᴏꜰꜰ 

<blockquote><b>👮 ᴀᴅᴍɪɴ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</b></blockquote>

<b>›› /add_admin :</b> ᴀᴅᴅ ᴀ ɴᴇᴡ ᴀᴅᴍɪɴ  
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ 
<b>›› /admins :</b> ʟɪꜱᴛ ᴀʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴅᴍɪɴꜱ   

<blockquote><b>⭐ ᴘʀᴇᴍɪᴜᴍ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</b></blockquote>

<b>›› /addpremium :</b> ɢʀᴀɴᴛ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ ᴛᴏ ᴀ ᴜꜱᴇʀ   
<b>›› /premium_users :</b> ʟɪꜱᴛ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ   
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜰʀᴏᴍ ᴀ ᴜꜱᴇʀ   
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None ) #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>For More Join - <a href='https://t.me/+AdcXPREPNEpkZmNl'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> </b>"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "Minato_Sencie")
UPI_ID = os.environ.get("UPI_ID", "sanjaykingboy9597-1@okicici")
QR_PIC = os.environ.get("QR_PIC", "https://files.catbox.moe/v81935.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"https://t.me/Minato_Sencie")
#--------------------------------------------
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "40 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "100 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "280 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "480 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "880 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
