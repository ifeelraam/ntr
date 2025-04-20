from pyrogram import Client
from pyrogram.types import Message
from utils.db import save_user_or_group
from utils.force_sub import check_force_sub

START_TEXT = (
    "*Hey!*\n"
    "> I’m your Billa kang assistant — add me to a group or reply with a sticker/image/video to create sticker packs."
    "\n\n_Use /kang, /kangurl or /videokang._"
)

async def handle_start(client: Client, message: Message):
    chat = message.chat
    await save_user_or_group(chat)

    # Check force sub (multi-channel)
    fsub_status = await check_force_sub(client, message.from_user.id)
    if not fsub_status["ok"]:
        await message.reply_text(fsub_status["message"], disable_web_page_preview=True)
        return

    await message.reply_text(START_TEXT, parse_mode="markdown")
