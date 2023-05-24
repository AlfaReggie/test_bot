from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram import types
from aiogram.utils import executor

text = ['Редис', 'Помидор', 'Огурец']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)