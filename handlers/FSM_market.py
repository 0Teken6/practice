from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import buttons
from db import main_db


class RegisterProduct(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    productid = State()
    infoproduct = State()
    collection = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    await RegisterProduct.name.set()
    await message.answer(text='Write the name of product:', reply_markup=buttons.cancel)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Write size:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Write category:')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Write price:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Write Product ID:')


async def load_productid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['productid'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Write info of product:')


async def load_infoproduct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['infoproduct'] = message.text

    await RegisterProduct.next()
    await message.answer(text='Write collection:')


async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text

    await RegisterProduct.next()
    kb = types.ReplyKeyboardRemove()
    await message.answer(text='Send photo:', reply_markup=kb)


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    keyboard = ReplyKeyboardMarkup(row_width=2)
    keyboard.add(KeyboardButton('Yes'), KeyboardButton('No'))

    await RegisterProduct.next()
    await message.answer_photo(photo=data['photo'],
                               caption=f'Name: {data["name"]}\n'
                                       f'Size: {data["size"]}\n'
                                       f'Category: {data["category"]}\n'
                                       f'Price: {data["price"]}\n'
                                       f'Product ID: {data["productid"]}\n'
                                       f'Product Info: {data["infoproduct"]}\n'
                                       f'Collection: {data["collection"]}\n\n'
                                       f'<b>Is it correct?</b>',
                               reply_markup=keyboard, parse_mode=types.ParseMode.HTML)


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Yes':
        async with state.proxy() as data:
            await main_db.sql_insert_market(
                name=data['name'],
                size=data['size'],
                price=data['price'],
                productid=data['productid'],
                category=data['category'],
                infoproduct=data['infoproduct'],
                collection=data['collection'],
                photo=data['photo'],
            )

            await message.answer('Data is saved!', reply_markup=buttons.start_buttons)
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
    dp.register_message_handler(fsm_start, commands=['register_product'])
    dp.register_message_handler(load_name, state=RegisterProduct.name)
    dp.register_message_handler(load_size, state=RegisterProduct.size)
    dp.register_message_handler(load_price, state=RegisterProduct.price)
    dp.register_message_handler(load_category, state=RegisterProduct.category)
    dp.register_message_handler(load_productid, state=RegisterProduct.productid)
    dp.register_message_handler(load_infoproduct, state=RegisterProduct.infoproduct)
    dp.register_message_handler(load_collection, state=RegisterProduct.collection)
    dp.register_message_handler(load_photo, state=RegisterProduct.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=RegisterProduct.submit)