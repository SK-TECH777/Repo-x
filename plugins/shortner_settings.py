import requests
import random
import string
from config import SHORTLINK_URL, SHORTLINK_API, TUT_VID
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    InputMediaPhoto
)
from pyrogram.errors.pyromod import ListenerTimeout

# ------------------------------------------------------------
# Generate alias for short URL API
# ------------------------------------------------------------
def generate_random_alphanumeric():
    import string, random
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(8))


# ------------------------------------------------------------
# Short link generator (always fetch settings from DB)
# ------------------------------------------------------------
async def get_short(url, client):
    cfg = await client.mongodb.get_shortner_config()

    if not cfg.get("shortner_enabled", True):
        return url

    short_url = cfg.get("short_url", SHORTLINK_URL)
    short_api = cfg.get("short_api", SHORTLINK_API)

    alias = generate_random_alphanumeric()

    try:
        api_url = f"https://{short_url}/api?api={short_api}&url={url}&alias={alias}"
        r = requests.get(api_url, timeout=10)
        data = r.json()

        if r.status_code == 200 and data.get("status") == "success":
            return data.get("shortenedUrl", url)
    except Exception:
        pass

    return url


# ------------------------------------------------------------
# /shortner COMMAND
# ------------------------------------------------------------
@Client.on_message(filters.command("shortner") & filters.private)
async def shortner_cmd(client, message):
    if message.from_user.id not in client.admins:
        return await message.reply("❌ Only admins can use this.")
    await shortner_panel(client, message)


# ------------------------------------------------------------
# Shortner settings panel (always DB-driven)
# ------------------------------------------------------------
async def shortner_panel(client, query_or_message):

    cfg = await client.mongodb.get_shortner_config()

    short_url = cfg.get("short_url", SHORTLINK_URL)
    short_api = cfg.get("short_api", SHORTLINK_API)
    tutorial = cfg.get("tutorial_link", TUT_VID)
    enabled = cfg.get("shortner_enabled", True)

    # test API
    if enabled:
        try:
            test = requests.get(
                f"https://{short_url}/api?api={short_api}&url=https://google.com&alias=test",
                timeout=4
            )
            status = "✓ WORKING" if test.status_code == 200 else "✗ NOT WORKING"
        except:
            status = "✗ NOT WORKING"
    else:
        status = "✗ DISABLED"

    toggle_text = "Turn OFF" if enabled else "Turn ON"

    msg = f"""
<b>✦ SHORTNER SETTINGS</b>

<b>Current Settings:</b>
• Status: {"Enabled" if enabled else "Disabled"}
• Shortner URL: <code>{short_url}</code>
• Shortner API: <code>{short_api}</code>
• Tutorial Link: <code>{tutorial}</code>

<b>API Status:</b> {status}
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(toggle_text, "toggle_shortner"),
            InlineKeyboardButton("Add Shortner", "add_shortner")
        ],
        [
            InlineKeyboardButton("Set Tutorial Link", "set_tutorial_link")
        ],
        [
            InlineKeyboardButton("Test Shortner", "test_shortner")
        ],
        [
            InlineKeyboardButton("« Back", "settings")
        ]
    ])

    img = "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"

    if hasattr(query_or_message, "message"):
        await query_or_message.message.edit_media(
            media=InputMediaPhoto(img, caption=msg),
            reply_markup=keyboard
        )
    else:
        await query_or_message.reply_photo(img, caption=msg, reply_markup=keyboard)


# ------------------------------------------------------------
# Open panel from button
# ------------------------------------------------------------
@Client.on_callback_query(filters.regex("^shortner$"))
async def shortner_cb(client, query):
    if query.from_user.id not in client.admins:
        return await query.answer("Admins only!", show_alert=True)
    await shortner_panel(client, query)


# ------------------------------------------------------------
# Toggle shortner status (database only)
# ------------------------------------------------------------
@Client.on_callback_query(filters.regex("^toggle_shortner$"))
async def toggle_shortner(client, query):
    if query.from_user.id not in client.admins:
        return await query.answer("Admins only!", show_alert=True)

    cfg = await client.mongodb.get_shortner_config()
    new_status = not cfg.get("shortner_enabled", True)

    await client.mongodb.set_shortner_status(new_status)

    await query.answer("Updated!")
    await shortner_panel(client, query)


# ------------------------------------------------------------
# Add shortner details (db only)
# ------------------------------------------------------------
@Client.on_callback_query(filters.regex("^add_shortner$"))
async def add_shortner(client, query):
    if query.from_user.id not in client.admins:
        return await query.answer("Admins only!", show_alert=True)

    await query.message.edit_text(
        "**Send shortner details in this format:**\n\n"
        "`domain.com APIKEY`"
    )

    try:
        res = await client.listen(query.from_user.id, filters=filters.text, timeout=60)
        text = res.text.strip()

        parts = text.split()
        if len(parts) < 2:
            raise ValueError

        new_url = parts[0].replace("https://", "").replace("http://", "").replace("/", "")
        new_api = " ".join(parts[1:])

        await client.mongodb.update_shortner_setting("short_url", new_url)
        await client.mongodb.update_shortner_setting("short_api", new_api)

        await query.message.edit_text(
            f"**Shortner Updated!**\nURL: `{new_url}`\nAPI: `{new_api[:20]}...`",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("« Back", "shortner")]])
        )

    except Exception:
        await query.message.edit_text(
            "**Invalid Format!**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("« Back", "shortner")]])
        )


# ------------------------------------------------------------
# Set tutorial link (db only)
# ------------------------------------------------------------
@Client.on_callback_query(filters.regex("^set_tutorial_link$"))
async def set_tutorial(client, query):
    if query.from_user.id not in client.admins:
        return await query.answer("Admins only!", show_alert=True)

    await query.message.edit_text("Send new tutorial link:")

    try:
        res = await client.listen(query.from_user.id, filters=filters.text, timeout=60)
        new_link = res.text.strip()

        await client.mongodb.update_shortner_setting("tutorial_link", new_link)

        await query.message.edit_text(
            "Tutorial link updated!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("« Back", "shortner")]])
        )

    except ListenerTimeout:
        await query.message.edit_text(
            "Timeout!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("« Back", "shortner")]])
        )


# ------------------------------------------------------------
# Test shortner API (db only)
# ------------------------------------------------------------
@Client.on_callback_query(filters.regex("^test_shortner$"))
async def test_shortner(client, query):
    if query.from_user.id not in client.admins:
        return await query.answer("Admins only!", show_alert=True)

    await query.message.edit_text("Testing shortner...")

    cfg = await client.mongodb.get_shortner_config()

    short_url = cfg.get("short_url", SHORTLINK_URL)
    short_api = cfg.get("short_api", SHORTLINK_API)

    test_url = "https://google.com"
    alias = generate_random_alphanumeric()

    try:
        api_url = f"https://{short_url}/api?api={short_api}&url={test_url}&alias={alias}"

        r = requests.get(api_url, timeout=10)
        data = r.json()

        if r.status_code == 200 and data.get("status") == "success":
            msg = f"**Success!**\nShort URL: `{data.get('shortenedUrl')}`"
        else:
            msg = f"**Failed!** Error: `{data.get('message')}`"

    except Exception as e:
        msg = f"**Error:** `{str(e)}`"

    await query.message.edit_text(
        msg,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("« Back", "shortner")]])
  )
