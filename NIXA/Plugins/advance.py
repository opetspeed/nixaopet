import os
import asyncio
import sys
import git
import heroku3
from NIXA.main import BOT
from config import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
hl = '/'
nixaversion = '3.0'

NIXA_PIC = "https://te.legra.ph/file/084c206996897e2d42443.jpg"
  

NIXA = f"""
    ᴍᴜsɪᴄ sᴘᴀᴍ ʙᴏᴛ\n\n
┌──────────────────
│➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.1`
│➠ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`
│➠ **ʙᴏᴛ vᴇʀsɪᴏɴ**  : `{nixaversion}`
└──────────────────\n\n """  

                                  
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
     await BOT.send_file(event.chat_id,
                                  NIXA_PIC,
                                  caption=NIXA,
                                  buttons=[
        [
        Button.url("🎓 ᴄʜᴀɴɴᴇʟ", "https://t.me/TheBotsUpdate"),
        Button.url("🎌 sᴜᴘᴘᴏʀᴛ", "https://t.me/TheSupportBots")
        ],
        [
        Button.url("💸 ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ", "https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
        start = datetime.now()
        text = "ᴘᴏɴɢ!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🎉 𝗣 𝗢 𝗡 𝗚 !!\n\n♡︎ `{ms}` ᴍs ♡︎")
        
        

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**ʀᴇʙᴏᴏᴛɪɴɢ ↪️**.. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟ ɪᴛ sᴛᴀʀᴛs ᴀɢᴀɪɴ"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await BOT.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

