import os
import wget
import speedtest
from PIL import Image
from pyrogram.types import Message
from pyrogram import filters, Client
from NIXA.main import bot as app
from config import SUDO_USERS as SUDOERS

@app.on_message(filters.command("speedtest") & ~filters.edited)
async def run_speedtest(_, message):
    userid = message.from_user.id
    m = await message.reply_text("⇋ ᴘʀᴏᴄᴇssɪɴɢ...")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⇋ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ")
        test.download()
        m = await m.edit("⇋ ʀᴜɴɴɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ")
        test.upload()
        test.results.share()
    except speedtest.ShareResultsConnectFailure:
        pass
    except Exception as e:
        await m.edit_text(e)
        return
    result = test.results.dict()
    m = await m.edit_text("⇋ sʜᴀʀɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ")
    if result["share"]:
        path = wget.download(result["share"])
        try:
            img = Image.open(path)
            c = img.crop((17, 11, 727, 389))
            c.save(path)
        except BaseException:
            pass
    output = f"""
┌─────────────────────
│➺ **sᴘᴇᴇᴅ ᴛᴇsᴛ ʀᴇsᴜʟᴛs**
│    
│✱<u>**ᴄʟɪᴇɴᴛ:**</u>
│➤**ɪsᴘ:** {result['client']['isp']}
│➤**ᴄᴏᴜɴᴛʀʏ:** {result['client']['country']}
│ 
│✱<u>**sᴇʀᴠᴇʀ:**</u>
│
│➤**ɴᴀᴍᴇ:** {result['server']['name']}
│➤**ᴄᴏᴜɴᴛʀʏ:** {result['server']['country']}, {result['server']['cc']}
│➤**sᴘᴏɴsᴏʀ:** {result['server']['sponsor']}
│➤**ʟᴀᴛᴇɴᴄʏ:** {result['server']['latency']}  
│➤**ᴘ ᴏ ɴ ɢ:** {result['ping']}
└─────────────────────
"""
    if result["share"]:
        msg = await app.send_photo(
            chat_id=message.chat.id, photo=path, caption=output
        )
        os.remove(path)
    else:
        msg = await app.send_message(
            chat_id=message.chat.id, text=output
        )
    await m.delete() 
