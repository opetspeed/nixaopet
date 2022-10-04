import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from NIXA.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT, BOT_USERNAME


ALIVE_PIC = START_PIC
HOME_TEXT = " **ʜᴇʟʟᴏ sɪʀ [{}](tg://user?id={})** \n\n**ᴛʜɪꜱ ʙᴏᴛ ʜᴀꜱ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.** **ᴀɴᴅ ᴛʜɪꜱ ᴍᴜꜱɪᴄ + ꜱᴘᴀᴍ + ᴠᴄʀᴀɪᴅ ʙᴏᴛ ꜱᴍᴀꜱʜ ᴛʜᴇᴍ ᴏꜰ ᴀʟʟ ꜱᴇʀᴠᴇʀ ᴏꜰ ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀꜱꜱ | ᴘᴏᴡᴇʀᴇᴅ ʙʏ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](t.me/Mr_DiSasTer_XD)**"
HELP_TEXT = """ᴛʜɪꜱ ʙᴏᴛ ʜᴀꜱ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.ᴀɴᴅ ᴛʜɪꜱ ᴍᴜꜱɪᴄ + ꜱᴘᴀᴍ + ᴠᴄʀᴀɪᴅ ʙᴏᴛ ꜱᴍᴀꜱʜ ᴛʜᴇᴍ ᴏꜰ ᴀʟʟ ꜱᴇʀᴠᴇʀ ᴏꜰ ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀꜱꜱ | ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ᴛᴇᴄʜ ǫᴜᴀʀᴅ](t.me/TechQuard)
❄ **sᴇᴛᴜᴘ ɢᴜɪᴅᴇ** :

➠ sᴛᴀʀᴛ ᴀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
➠ ᴀᴅᴅ ʙᴏᴛ ᴀɴᴅ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ɪɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
➠ ᴅᴏɴᴇ sᴇᴛᴜᴘ ᴘʀᴏᴄᴇss ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅs ʙᴇʟᴏᴡ.
"""



USER_TEXT = """
👀 **ᴜsᴇʀs ᴄᴏᴍᴍᴀɴᴅs** :
➠ /id - ᴛᴏ ɢᴇᴛ ᴜsᴇʀ ɪᴅ ᴀɴᴅ ᴄʜᴀᴛ ɪᴅ.
➠ /info - ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
➠ /tg - ᴛᴏ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ɪᴍɢ ʟɪɴᴋ.
➠ /play - ᴛʏᴘᴇ ᴛʜɪs ᴡɪᴛʜ ɢɪᴠᴇ ᴛʜᴇ sᴏɴɢ ᴛɪᴛʟᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ. (ʀᴇᴍᴇᴍʙᴇʀ ᴛᴏ ᴅᴏɴ'ᴛ ᴘʟᴀʏ ʏᴏᴜᴛᴜʙᴇ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ !!, ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴡɪʟʟ ᴄᴀᴜsᴇ ᴜɴғᴏʀᴇsᴇᴇɴ ᴘʀᴏʙʟᴇᴍs.)
➠ /vplay - ᴛʏᴘᴇ ᴛʜɪs ᴡɪᴛʜ ɢɪᴠᴇ ᴛʜᴇ sᴏɴɢ ᴛɪᴛʟᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ. (ʀᴇᴍᴇᴍʙᴇʀ ᴛᴏ ᴅᴏɴ'ᴛ ᴘʟᴀʏ ʏᴏᴜᴛᴜʙᴇ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ !!, ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴡɪʟʟ ᴄᴀᴜsᴇ ᴜɴғᴏʀᴇsᴇᴇɴ ᴘʀᴏʙʟᴇᴍs.)
➠ /stream <ʟɪᴠᴇ ᴜʀʟ> ᴛᴏ ᴘʟᴀʏ ʟɪᴠᴇ sᴛʀᴇᴀᴍs.
➠ /vstream - ᴛʏᴘᴇ ᴛʜɪs ᴡɪᴛʜ ɢɪᴠᴇ ᴛʜᴇ ʏᴏᴜᴛᴜʙᴇ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ᴠɪᴅᴇᴏ ʟɪɴᴋ ᴏʀ ᴍ3ᴜ8 ʟɪɴᴋ ᴛᴏ ᴘʟᴀʏ ʟɪᴠᴇ ᴠɪᴅᴇᴏ. (ʀᴇᴍᴇʙᴇʀ ᴛᴏ ᴅᴏɴ'ᴛ ᴘʟᴀʏ ʟᴏᴄᴀʟ ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ ғɪʟᴇs ᴏʀ ɴᴏɴ-ʟɪᴠᴇ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ, ʙᴇᴄᴀᴜsᴇ ɪᴛ ᴡɪʟʟ ᴄᴀᴜsᴇ ᴜɴғᴏʀᴇsᴇᴇɴ ᴘʀᴏʙʟᴇᴍs.)
➠ /song ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀ ᴀᴜᴅɪᴏ ғɪʟᴇ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ.  
➠ /video ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ. 
➠ /lyric ᴛᴏ ғɪɴᴅ ʟʏʀɪᴄs.
➠ /speedtest - ᴛᴏ ɢᴇᴛ sᴘᴇᴇᴅᴛᴇsᴛ.[sᴜᴅᴏ ᴜsᴇʀ ᴏɴʟʏ]

"""

SPAM_TEXT = """
🍃 **ʜᴇʀᴇ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴇ ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs** :

➠ /spam - <ᴄᴏᴜɴᴛ> ᴛᴇxᴛ ᴛᴏ sᴘᴀᴍ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ.
➠ /delspam - <ᴄᴏᴜɴᴛ> ᴛᴇxᴛ ғᴏʀ sᴘᴀᴍᴍɪɴɢ.
➠ /fastspam - <ᴄount> ᴛᴇxᴛ ғᴏʀ ғᴀsᴛ sᴘᴀᴍ.
➠ /slowspam - <ᴄount> ᴛᴇxᴛ ғᴏʀ sʟᴏᴡ sᴘᴀᴍ.
➠ /delayspam - <ᴄount> ᴛᴇxᴛ ғᴏʀ sᴘᴀᴍᴍɪɴɢ.
➠ /raid - <ᴄount> ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴀɪᴅ.
➠ /replyraid - ᴛʜɪs ᴄᴍᴅ ʀᴇᴘʟʏʀᴀɪᴅ ᴀᴄᴛɪᴠᴀᴛᴇᴅ.
➠ /dreplyraid - ᴛʜɪs ᴄᴍᴅ ᴜsᴇ ғᴏʀ sᴛᴏᴘɪɴɢ ʀᴇᴘʟʏʀᴀɪᴅ.
➠ /loveraid - <ᴄount> ᴛʜɪs ᴄᴍᴅ ʀᴜɴ ʟᴏᴠᴇʀᴀɪᴅ.
➠ /lovereplyraid - ᴛʜɪs ᴄᴍᴅ ᴀᴄᴛɪᴠᴇ ᴀᴜᴛᴏ ʟᴏᴠᴇʀᴀɪᴅ
➠ /dlovereplyraid - ᴛʜɪs ᴄᴍᴅ ᴜsᴇ ғᴏʀ sᴛᴏᴘ ʀᴇᴘʟʏ ʟᴏᴠᴇʀᴀɪᴅ

"""

VCRAID_TEXT = """
🌾 **ʜᴇʀᴇ ᴠᴄʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs ᴜsᴇ ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs** :

➠ /vcraid <chatid> - ɢɪᴠᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ᴇʟsᴇ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴠᴏɪᴄᴇ ʀᴀɪᴅ.
➠ /vcraidpause - ᴛᴏ ᴘᴀᴜsᴇ ʀᴀɪᴅ.
➠ /vcraidresume ᴛᴏ ʀᴇsᴜᴍᴇ ʀᴀɪᴅ.
➠ /vcraidend <chatid> ᴛᴏ ᴇɴᴅ ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ ʀᴀɪᴅ.
"""

ADMIN_TEXT = """
🍂 **ᴀᴅᴍɪɴs ᴄᴏᴍᴍᴀɴᴅs** :

➠ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ.
➠ /end ᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍɪɴɢ.
➠ /pause ᴛᴏ ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ.
➠ /resume ᴛᴏ ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ.
➠ /volume ᴛᴏ sᴇᴛ ᴠᴏʟᴜᴍᴇ.
➠ /skip ᴛᴏ sᴋɪᴘ ᴛʀᴀᴄᴋs.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("🍃 ᴜsᴇʀs", callback_data="users_cmd"),              
                InlineKeyboardButton("🌾 ᴀᴅᴍɪɴs", callback_data="admins_cmd"),
                InlineKeyboardButton("👀 sᴜᴅᴏ ", callback_data="sudo_cmd"),
            ],
            [
                InlineKeyboardButton(" ʙᴀᴄᴋ ", callback_data="home"),
                InlineKeyboardButton("⟳ ᴄʟᴏꜱᴇ ⟲", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("📢 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/TheBotsUpdate"),
            ],
            [
                InlineKeyboardButton("📄 ʜᴇʟᴘ ᴀɴᴅ ᴄᴍᴅ", callback_data="help"),
                InlineKeyboardButton("🌾 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/Sumit9969/NixaMusicBot"),
                
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users_cmd":
        buttons = [
            [
                InlineKeyboardButton("◁", callback_data="help"),
                InlineKeyboardButton("⟳ ᴄʟᴏꜱᴇ ⟲", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
     
     

    elif query.data=="admins_cmd":
        buttons = [
            [
                InlineKeyboardButton("◁", callback_data="help"),
                InlineKeyboardButton("⟳ ᴄʟᴏꜱᴇ ⟲", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ADMIN_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="sudo_cmd":
        buttons = [
            [
                InlineKeyboardButton("🍒 sᴘᴀᴍ", callback_data="spam_cmd"),
                InlineKeyboardButton("🎟️ ᴠᴄʀᴀɪᴅ", callback_data="vcraid_cmd"),
            ],
            [
                InlineKeyboardButton("◁", callback_data="help"),
                InlineKeyboardButton("⟳ ᴄʟᴏꜱᴇ ⟲", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="spam_cmd":
        buttons = [
            [
                InlineKeyboardButton("◁", callback_data="sudo_cmd"),
                InlineKeyboardButton("⟳ ᴄʟᴏꜱᴇ ⟲", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SPAM_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="vcraid_cmd":
        buttons = [
            [
                InlineKeyboardButton("◁", callback_data="sudo_cmd"),
                InlineKeyboardButton("⟳ ᴄʟᴏꜱᴇ ⟲", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                VCRAID_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons =  [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("📢 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/TheBotsUpdate"),
            ],
            [
                InlineKeyboardButton("📄 ʜᴇʟᴘ ᴀɴᴅ ᴄᴍᴅ", callback_data="help"),
                InlineKeyboardButton("🌾 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/Sumit9969/NixaMusicBot"),
                
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client: Client, message: Message):
    get_me = await client.get_me()
    self.username = get_me.username
    buttons =  [
            [
                InlineKeyboardButton("🍃 ᴜsᴇʀs", callback_data="users_cmd"),              
                InlineKeyboardButton("🌾 ᴀᴅᴍɪɴs", callback_data="admins_cmd"),
                InlineKeyboardButton("👀 sᴜᴅᴏ ", callback_data="sudo_cmd"),
            ],
            [
                InlineKeyboardButton(" ʙᴀᴄᴋ ", callback_data="home"),
                InlineKeyboardButton("⟳ ᴄʟᴏꜱᴇ ⟲", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=f"{HELP_TEXT}", reply_markup=reply_markup)
