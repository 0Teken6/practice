from aiogram.dispatcher import Dispatcher
from aiogram import types


async def start(message: types.Message):
    await message.answer(f'Hi {message.from_user.full_name}!')


async def info(message: types.Message):
    await message.answer(f'It is a practice bot for market')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])

