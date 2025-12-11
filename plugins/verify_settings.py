from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.database import *

VERIFY_KEY = "VERIFY_MODE"


@Client.on_message(filters.command("verifysettings") & filters.private)
async def verify_settings_cmd(client, message):
    mode = await db.get_val(VERIFY_KEY)
    status = "ON" if mode else "OFF"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Turn OFF" if mode else "Turn ON", callback_data="toggle_verify")],
        [InlineKeyboardButton("Close", callback_data="close_verify")]
    ])

    await message.reply(
        f"🔐 VERIFY MODE is currently: **{status}**",
        reply_markup=keyboard
    )


@Client.on_callback_query(filters.regex("^toggle_verify$"))
async def toggle_verify_cb(client, query: CallbackQuery):
    mode = await db.get_val(VERIFY_KEY)
    new_status = not mode

    await db.update_val(VERIFY_KEY, new_status)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Turn OFF" if new_status else "Turn ON", callback_data="toggle_verify")],
        [InlineKeyboardButton("Close", callback_data="close_verify")]
    ])

    await query.message.edit_text(
        f"🔐 VERIFY MODE is now: **{'ON' if new_status else 'OFF'}**",
        reply_markup=keyboard
    )
    await query.answer()


@Client.on_callback_query(filters.regex("^close_verify$"))
async def close_verify_cb(client, query: CallbackQuery):
    await query.answer()
    await query.message.delete()
