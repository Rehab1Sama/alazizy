import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "5660372064:AAHEwKNeKUX-zNA0W0AVjcrFMzwvhiyrfFg")
BOT_NAME = getenv("BOT_NAME", "Jezal")
API_ID = int(getenv("API_ID", "25646040"))
API_HASH = getenv("API_HASH", "5e1ea380a54ced6eb364f6d10efbcb70")
OWNER_NAME = getenv("OWNER_NAME", "Rehab")
ALIVE_NAME = getenv("ALIVE_NAME", "Rehab Jezal")
BOT_USERNAME = getenv("BOT_USERNAME", "Jezal123_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "JezalBot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rhbfh65")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "J_ezal")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/06b651dc0d827b6887764.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RAZANALYAFAE/AQANI")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/19d68d531fd2f6f96e368.jpg")
