
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
    
from telegram.ext import CallbackContext
__mod_name__ = "➕ ᴠᴄ ᴇxᴛʀᴀ"

__help__ ="""**Extra  Commands:**
/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

**Group Settings:**
/settings - Get a complete group's settings with inline buttons
🔗 **Options in Settings:**
1️⃣ You can set **Audio Quality** you want to stream on voice chat.
2️⃣ You can set **Video Quality** you want to stream on voice chat.
3️⃣ **Auth Users**:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)
4️⃣ **Clean Mode:** When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.
5️⃣ **Command Clean** : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.
6️⃣ Team Undanpirapu

**Play Settings:**
/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 
Options in playmode:
1️⃣ **Search Mode** [Direct or Inline] - Changes your search mode while you give /play mode. 
2️⃣ **Admin Commands** [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)
3️⃣ **Play Type** [Everyone or Admins] - If admins, only admins present in group can play music on voice chat."""
