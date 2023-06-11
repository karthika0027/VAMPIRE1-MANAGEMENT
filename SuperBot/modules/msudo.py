from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
    
from telegram.ext import CallbackContext
__mod_name__ = "🃏 ᴠᴄ ꜱᴜᴅᴏ"

__help__ ="""🔰**ADD & REMOVE SUDO USERS :**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**HEROKU:**
/usage - Dyno Usage.

🌐**CONFIG VARS:**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**BOT COMMANDS:**
/reboot - Reboot your Bot. 
/update - Update Bot.
/mspeedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**STATS COMMANDS:**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**BLACKLIST CHAT FUNCTION:**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**BLOCKED FUNCTION:**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**GBAN FUNCTION:**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**VIDEOCALLS FUNCTION:**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**PRIVATE BOT FUNCTION:**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**BROADCAST FUNCTION:**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.
options for broadcast:
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message
**Example:** `/broadcast -user -assistant -pin Hello Testing`
"""