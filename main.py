from config import dp, Admins, bot
from aiogram.utils import executor
import logging
from handlers import commands, echo, quiz, FSM_market, products_commands, admin_commands, webapp, admin_group, FSM_reg
from Google_Sheets import sheets
import buttons
from db import main_db


async def on_startup(_):
    for id in Admins:
        await admin_commands.set_scheduler()
        await bot.send_message(chat_id=id, text='Bot started', reply_markup=buttons.start_buttons)
        await main_db.sql_create()


async def on_shutdown(_):
    for id in Admins:
        await bot.send_message(chat_id=id, text='Bot is off')

commands.register_commands(dp)
FSM_reg.register_fsm_for_user(dp)
sheets.register_google_sheets(dp)
quiz.register_quiz(dp)
FSM_market.register_fsm_prod(dp)
products_commands.register_products_commands(dp)
webapp.register_webapp(dp)
admin_group.register_admin_group(dp)
# echo.register_echo(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
