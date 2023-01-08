from msonebot import bot
from msonebot.logging import LOGGER

LOGGER(__name__).info("client successfully initiated. ")
if __name__ == "__main__":
    bot.run()

