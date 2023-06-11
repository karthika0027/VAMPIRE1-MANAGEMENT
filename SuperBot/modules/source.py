from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from SuperBot import OWNER_USERNAME, dispatcher
from SuperBot import pbot as client

ANON = "https://te.legra.ph/file/087777b019b111a9f2bb7.jpg"


@client.on_message(filters.command(["repo","source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**
**» ɴᴇᴛᴡᴏʀᴋ :** @team_vampir
**» ᴍʏ ᴏᴡɴᴇʀ​ :** [MR. ᭄ 𝕋𝕀𝕄𝔼 𝕋ℝ𝔸𝕍𝔼𝕃𝕃𝔼ℝ😡⃝⃟➛⃟⃟⃝⃝❼½சனி𝕾𝖖𝖚𝖆𝖉࿐⁰⁰⁷](https://t.me/ROWDY_OF_PLUS)
**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [➳ᴹᴿ✿࿐𝑳𝑶𝑮𝑬𝑺𝑯⏤͟͟](https://t.me/cl_me_logesh)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ɴᴇᴛᴡᴏʀᴋ ᴏᴜʀ ᴄʜᴀᴛ ɢʀᴜᴏᴘ ᴀɴᴅ ᴇɴᴊᴏʏ ʏᴏᴜʀ ᴅᴀʏ. ᴍʏ ᴏᴡɴᴇʀ ꜱᴀᴛɪꜱꜰɪᴇꜱ ᴀʟʟ ʏᴏᴜʀ ꜰᴇᴇʟɪɴɢꜱ ꜱᴏ ɴᴇᴛᴡᴏʀᴋ**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "• ɴᴇᴛᴡᴏʀᴋ •",
                        url="https://t.me/TEAM_VAMPIR",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "🎗️ ᴀʙᴏᴜᴛ ᴍᴇ"
