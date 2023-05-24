from loader import dp, text
from aiogram import types

@dp.message_handler(text = text)
async def answer_start_command(message: types.Message):
    await message.answer(text = "Potatos bro!")
