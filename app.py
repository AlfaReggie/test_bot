from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = r"6239166068:AAFY6cEvAp5pvqcd2W9j893GVrwug2YOJtw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

text = ['Редис', 'Помидор', 'Огурец']

@dp.message_handler(commands = 'start')
async def answer_start_command(message: types.Message):
    await message.answer(text = f"Hi!"
                         f"\nGlad to see you!")

@dp.message_handler(commands = 'add')
async def answer_start_command(message: types.Message):
    await message.answer(text = "Add command reaction")

@dp.message_handler(text = text)
async def answer_start_command(message: types.Message):
    await message.answer(text = "Potatos bro!")

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
