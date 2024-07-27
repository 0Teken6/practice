from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(
    KeyboardButton('/start'),
    KeyboardButton('/info'),
    KeyboardButton('/register_product'),
    KeyboardButton('/order'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Cancel'))
