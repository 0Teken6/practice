from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import Staff, bot
import buttons


class RegisterOrder(StatesGroup):
    productid = State()
    size = State()
    quantity = State()
    phone = State()
    submit = State()


async def fsm_start(message: types.Message):
    await RegisterOrder.productid.set()
    await message.answer(text='Write the Product ID:', reply_markup=buttons.cancel)


async def load_productid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['productid'] = message.text

    await RegisterOrder.next()
    await message.answer(text='Write size:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await RegisterOrder.next()
    await message.answer(text='Write quantity:')


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await RegisterOrder.next()
    await message.answer(text='Write phone:')


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    keyboard = ReplyKeyboardMarkup(row_width=2)
    keyboard.add(KeyboardButton('Yes'), KeyboardButton('No'))

    await RegisterOrder.next()
    await message.answer(
        text=f'Product ID: {data["productid"]}\n'
             f'Size: {data["size"]}\n'
             f'Quantity: {data["quantity"]}\n'
             f'Phone: {data["phone"]}\n\n'
             f'<b>Is it correct?</b>',
        reply_markup=keyboard, parse_mode=types.ParseMode.HTML)



async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Yes':
        async with state.proxy() as data:
            for id in Staff:
                await bot.send_message(chat_id=id,
                    text=f'Order Info\n\n'
                         f'Product ID: {data["productid"]}\n'
                         f'Size: {data["size"]}\n'
                         f'Quantity: {data["quantity"]}\n'
                         f'Phone: {data["phone"]}\n',
                    parse_mode=types.ParseMode.HTML)

        await message.answer('Order is made!', reply_markup=buttons.start_buttons)
        await state.finish()
    elif message.text == 'No':
        await message.answer('Canceled!', reply_markup=buttons.start_buttons)
        await state.finish()
    else:
        await message.answer(text='Tap on a button!')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Canceled')


def register_fsm_prod(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Cancel',
                                                 ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['order'])
    dp.register_message_handler(load_productid, state=RegisterOrder.productid)
    dp.register_message_handler(load_size, state=RegisterOrder.size)
    dp.register_message_handler(load_quantity, state=RegisterOrder.quantity)
    dp.register_message_handler(load_phone, state=RegisterOrder.phone)
    dp.register_message_handler(submit, state=RegisterOrder.submit)
