import asyncio
import base64
import os
import random        
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from NIXA.Modules.data import RAID, REPLYRAID, BOT_OWNER, LOVEOP
from NIXA.main import BOT
from config import SUDO_USERS

OWNER_ID = SUDO_USERS
que = {}
hl = '/'

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ʀᴀɪᴅ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.raid <count> <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴜsᴇʀs>\n\n.raid <count> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>\n\nᴄᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        nixa = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(nixa) == 2:
            user = str(nixa[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(nixa[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(nixa[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ʀᴇᴘʟʏʀᴀɪᴅ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.replyraid <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴜsᴇʀ>\n\n.replyraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>."
    if e.sender_id in SUDO_USERS:
        nixa = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        SAMx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(nixa[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ"            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ"
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏʀᴀɪᴅ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.dreplyraid <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴜsᴇʀ>\n\n.dreplyraid <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        nixa = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(nixa[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def _(event):
   usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴅᴇʟᴀʏʀᴀɪᴅ \n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.delayraid <ᴅᴇʟᴀʏ> <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴜsᴇʀ>\n\n.delayraid <ᴅᴇʟᴀʏ> <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>\n\nᴄᴏᴜɴᴛ ᴀɴᴅ sʟᴇᴇᴘᴛɪᴍᴇ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         nixa = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(nixa) == 3:
             user = str(nixa[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in BOT_OWNER:
                    text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ."
                await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(nixa[1])
                 sleeptimet = sleeptimem = float(Deadly[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in BOT_OWNER:
                       text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) == OWNER_ID:
                       text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ."
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Deadly[0])
                   counter = int(nixa[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)



@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sloveraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ʟᴏᴠᴇ ʀᴀɪᴅ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.loveraid <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴜsᴇʀ>\n\n.loveraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>\n\nᴄᴏᴜɴᴛ ᴍᴜsᴛ ʙᴇ ᴀ ɪɴᴛᴇɢᴇʀ."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        nixa = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(nixa) == 2:
            user = str(nixa[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(nixa[0])
                for _ in range(counter):
                    reply = random.choice(LOVEOP)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(nixa[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(LOVEOP)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@BOT.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(LOVEOP)),
            reply_to=event.message.id,
        )


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%slovereplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ʟᴏᴠᴇ ʀᴇᴘʟʏʀᴀɪᴅ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.lovereplyraid <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴜsᴇʀs>\n\n.lovereplyraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>."
    if e.sender_id in SUDO_USERS:
        nixa = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        SAMx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(nixa[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ."            
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in BOT_OWNER:
                text = f"ɪ ᴄᴀɴ'ᴛ ʀᴀɪᴅ ᴏɴ ᴍʏ ʜᴜʙʙʏ, ᴍʏ sᴡᴇᴇᴛʜᴇᴀʀᴛ | ʙsᴅᴋ ᴋ ʏᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ʜᴀɪ ᴇsɴᴇ ʜɪ ᴍᴜᴊʜᴇ ʙɴᴀʏᴀ ᴇɴᴘᴇ ᴍᴀɪ ʀᴀɪᴅ ɴʜɪ ᴋʀ sᴋʜᴛɪ."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) == OWNER_ID:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ʙᴏᴛ."
                await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"ᴛʜɪs ɢᴜʏ ɪs ᴀ sᴜᴅᴏ ᴜsᴇʀ."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sdlovereplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴀɪᴅ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n.dlovereplyraid <ᴜsᴇʀɴᴀᴍᴇ ᴏғ ᴜsᴇʀ>\n\n.dlovereplyraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ>"
    global que
    if e.sender_id in SUDO_USERS:    
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        nixa = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(nixa[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    


