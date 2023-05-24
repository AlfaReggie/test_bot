from loader import dp
from aiogram import types
from keyboards import commands_default_keybord


@dp.message_handler(commands = 'start')
async def answer_start_command(message: types.Message):
    await message.answer(text = f"Hi!"
                         f"\nGlad to see you!",
                         reply_markup=commands_default_keybord)

@dp.message_handler(commands = 'add')
async def answer_start_command(message: types.Message):
    await message.answer(text = "Add command reaction")

@dp.message_handler(commands = 'delete')
async def answer_start_command(message: types.Message):
    await message.answer(text = "Delete command reaction")

@dp.message_handler(commands = 'all_commands')
async def answer_start_command(message: types.Message):
    await message.answer(text = "/start\n"
                                "/add\n"
                                "/delete")
