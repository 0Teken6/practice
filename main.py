from config import dp, Staff, bot
from aiogram.utils import executor
import logging
from handlers import common_commands, FSM_market, FSM_orders
import buttons
from db import main_db


async def on_startup(_):
    for id in Staff:
        await bot.send_message(chat_id=id, text='Bot started', reply_markup=buttons.start_buttons)
        await main_db.sql_create()


async def on_shutdown(_):
    for id in Staff:
        await bot.send_message(chat_id=id, text='Bot is off')

common_commands.register_commands(dp)
FSM_market.register_fsm_prod(dp)
FSM_orders.register_fsm_prod(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
