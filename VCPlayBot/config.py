import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBNO2G4zNRA13lcpAJ5D-FOy910EruvWg0AdsxDNdWsoyxTDv7MzztLgxajNF59bUbs_3iVMxnstHVTt8CO7XSm8WzhrGtRI_nt1FvG6U7r2NwXVCW-hYgOg7ISMjquZFP2G45frhnxSyYovKkkxjy6zBU6m_Rp9CnOoZSmMwmUokSmTDXO9nyy1c0gHXEc1LWmZHsvlRRVG_DE3drN73yVZ7WxOjG4OMFLq37LwVV-yvbKZX1gndYDAZGEF907qWudf9cwuGs9_lCOoJa25g3Dj5uEsYERa8Vm3r7YRBCYS5khyAYj6ySBeVJt-y5bC-TJC7nr2A_GPtcmMzj2a7IcZ1WA6wA")
BOT_TOKEN = getenv("BOT_TOKEN", "1653789420:AAGjLfTKP-7ZeYjO26VTt5HaDNGDthUVjJY")
BOT_NAME = getenv("BOT_NAME", "The VC Music Player")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kernel4vincechat")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/3346a6121d43c52595cf1.png")
admins = {}
API_ID = int(getenv("API_ID", 5067596))
API_HASH = getenv("API_HASH", "0c1c4340f006ea05763e3fe42da32b4f")
BOT_USERNAME = getenv("BOT_USERNAME", "thevcmusicplayerbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "thevcmusicplayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "kernel4vincechat")
PROJECT_NAME = getenv("PROJECT_NAME", "The VC Music Player")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/teamdaisyx/daisyxmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "CLDRFM-ZUWOQR-CKDGPB-QTRXGH-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1362497646 1733656811").split()))
