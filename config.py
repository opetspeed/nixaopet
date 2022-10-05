import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAQe9OEAuwzpmMXTDmlMSrDSRlG8nhxbRJDLlpMAEdR-4SCYh3lHo-cj6znHipduWYB2o3EMgFeCnCl8cw_1oFxR-088JbkKdsAw_s7kUopUy_M8oXpM2cTXXbtFXPbOZ9Pb1vR_MwlsIyQriMYUrPmbnSf2gsy1SwpTGcfe1CRBZem9vSez7w9udZ71pqvDthqoA564HoNW-tQXRjqkIgmOqgWtVTsrpWKf2kA0Y6140OouEuHiYMGth2vDqL8MwBLaUlt_8CNod2SvRs7k1iPXjWex58g9MVI2sUzwoW3twJyMmq196dbw5u1floxrOch0NV8MmJRTTZoqqdyLT4pAAAAAVTZ1jYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5502766272:AAHmEovz3N5yt8q-pUmDP6m0rOdKmGDgL2M")
BOT_NAME = getenv("BOT_NAME", "ᴀsᴛʀᴏ ✘ ʀᴏʙᴏᴛ")
API_ID = int(getenv("API_ID", "10349797"))
API_HASH = getenv("API_HASH", "79554098746a63dadd45d7176bed5ede")
OWNER_NAME = getenv("OWNER_NAME", "ㅤ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "nousernamefix")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "herantapibot")
OWNER_ID = getenv("OWNER_ID", "2027429081")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ᴀsᴛʀᴏᴋᴏɴᴛ")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AstroMusikk")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AstroMusikk")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2027429081").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/084c206996897e2d42443.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Sumit9969/NixaMusicBot")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cb0315c63c5fce38ae3eb.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
