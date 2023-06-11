from SuperBot import MUST_JOIN , pbot
from pyrogram import  filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@pbot.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: pbot, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"ʜᴇʏ ʙᴀʙʏ 😍, ɪ'ᴍ ʜᴀᴘᴘʏ ᴛᴏ ʜᴇᴀʀ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴍʏ ʜᴇʟᴘ😃, ʙᴜᴛ ᴘʟᴇᴀꜱᴇ ɴᴇᴛᴡᴏʀᴋ ɪɴ [⚔️ 𝘛𝘌𝘈𝘔 𝘜𝘋𝘈𝘕𝘗𝘐𝘙𝘈𝘗𝘗𝘜 ⚔️ T⊶M⊶ ⊶U⊶P]({link}) 🤗",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ 𝘛𝘌𝘈𝘔 𝘜𝘋𝘈𝘕𝘗𝘐𝘙𝘈𝘗𝘗𝘜  ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
