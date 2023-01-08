from asyncio import get_event_loop, new_event_loop, set_event_loop
from msonebot.config import BOT_TOKEN, API_ID, API_HASH
from msonebot.logging import LOGGER
from pyrogram import Client
import time
import sys

LOGGER(__name__).info("Starting msonebot....")
BotStartTime = time.time()

VERSION_ASCII ="""
  =============================================================
  You MUST need to be on python 3.7 or above, shutting down the bot...
  =============================================================
  """
  
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
	LOGGER(__name__).critical(VERSION_ASCII)
	sys.exit(1)


BANNER = """

███╗   ███╗███████╗ ██████╗ ███╗   ██╗███████╗██████╗  ██████╗ ████████╗
████╗ ████║██╔════╝██╔═══██╗████╗  ██║██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██╔████╔██║███████╗██║   ██║██╔██╗ ██║█████╗  ██████╔╝██║   ██║   ██║   
██║╚██╔╝██║╚════██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║   ██║   
██║ ╚═╝ ██║███████║╚██████╔╝██║ ╚████║███████╗██████╔╝╚██████╔╝   ██║   
╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝    ╚═╝   
																		
 
"""

# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20


try:
	loop = get_event_loop()
except RuntimeError:
	set_event_loop(new_event_loop())
	loop = get_event_loop()

LOGGER(__name__).info(BANNER)
LOGGER(__name__).info("initiating the client")


plugins = dict(root="msonebot/plugins")
bot = Client(
	"msonebot",
	api_id=API_ID,
	api_hash=API_HASH,
	bot_token=BOT_TOKEN,
	plugins=plugins)  #https://docs.pyrogram.org/topics/smart-plugins
