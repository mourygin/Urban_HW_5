
#coding=UTF-8
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = '...............................................'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
btn_calc = KeyboardButton(text = 'Рассчитать')
btn_info = KeyboardButton(text = 'Информация')
kb.add(btn_calc)
kb.add(btn_info)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# @dp.message_handler(state=UserState.age)
# async def set_age(message, state):
#     await state.update_data(age = message.text)
#     await message.answer('Сообщите, пожалуйста, Ваш рост.')
#     await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Сообщите, пожалуйста, Ваш вес.')
    await UserState.weight.set()

@dp.message_handler(state=UserState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)
    await message.answer('Сообщите, пожалуйста, Ваш рост.')
    await UserState.growth.set()

@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
    await state.update_data(weight = message.text)
    # await message.get_data()
    data = await  state.get_data()
    calories = comp_caloryes(data['age'],data['growth'],data['weight'])
    await message.answer(f'Ваша суточная норма калорий:\n{int(calories[0])}, если Вы мужчина, или\n{int(calories[1])}, если Вы женщина.')

def comp_caloryes(age, growth, weight):
    result = int(weight) * 10 + int(growth) * 6.25 - int(age) * 5
    return result+5, result-161


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий Вашему здоровью.\n', reply_markup=kb)
    # await UserState.age.set()

@dp.message_handler(text='Рассчитать')
async def set_age(message, state):
    await state.update_data(age=message.text)
    await message.answer('Сообщите, пожалуйста, Ваш возраст.')
    await UserState.age.set()

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Данный бот разработан в качестве учебной задачи в ходе изучения языка Python.')

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    u_state = UserState()
    executor.start_polling(dp, skip_updates=True)