import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = int(os.getenv("API_ID", "12995565"))
API_HASH = os.getenv("API_HASH", "f43e63c6eb71cd9ee988e3b13a509f1a")
SESSION = os.getenv("SESSION", "BQAq7r_wO_ViPVVfH_rrlwkIbqaYQ0xjPMj4Kap2Y0Bzxw9rtKMJlbx6xm9I43fqTGBcnjjhkm08zpgy50YpbfF8lXqSjGjxFrA32MgE1BP4ichBCDCUU-0qf3IGi5RGaYuoX8tZDccEu7vifQAQxeOLKktpkWjmPAGalk8d3jyKojIaKaUInijSsjUsyRjBgDtzkmz_t2FbwNhW-D1OFibbiUjbVwio9f1JBSBASJWslrhh_FG2vIDckR29_Z2_DbU2GT3DPdpLR_-f6wIqAMkxChDWO-TAgJAVSSdelHPC31pPRRO0L12Q-zKj0cNpeA2SLh9X24sEx-ZbE8XQ8UvuAAAAATrsoq4A")
OWNER = os.getenv("OWNER", "1920507972")
OWNER_NAME = os.getenv("OWNER_NAME", "Shubhanshutya")
HNDLR = os.getenv("HNDLR", "!")
PING_PIC = os.getenv("PING_PIC", "https://telegra.ph/file/bd02cdf26f918a133d7c2.jpg") 
THUMB_PIC = os.getenv("THUMB_PIC", "https://telegra.ph/file/bd02cdf26f918a133d7c2.jpg")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1920507972").split()))
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
