import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from api.handlers import router
from db.repository import init_db

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await init_db()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
