
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

# Pegando o token do ambiente
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Inteligência ativada")

if __name__ == '__main__':
    executor.start_polling(dp)
