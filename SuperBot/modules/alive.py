import random

from pyrogram import __version__ as pyrover
from telegram import __version__ as telever
from telethon import Button
from telethon import __version__ as tlhver

from SuperBot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from SuperBot import telethn as tbot
from SuperBot.events import register

PHOTO = [
    "https://telegra.ph/file/6a21ea6677342f43b363e.jpg",
    "https://telegra.ph/file/40eb1ed850cdea274693e.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ {dispatcher.bot.first_name}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴏᴡɴᴇʀ​ : [[MR. ᭄ 𝙷𝙰𝙲𝙺𝙴𝚁😡⃝⃟➛⃟⃟⃝⃝❼½சனி𝕾𝖖𝖚𝖆𝖉࿐⁰⁰⁷](https://t.me/hackerofrip)](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "🙋‍♀️ Aʟɪᴠᴇ"
