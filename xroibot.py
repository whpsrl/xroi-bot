import os
from aiogram import Bot, Dispatcher, types, executor
import logging

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("✅ Bot attivo! Benvenuto nel sistema XROI Affiliate.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
