import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import TELEGRAM_BOT_TOKEN
from handlers import commands, messages

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(messages.router)

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())