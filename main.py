from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StateFilter
from aiogram import F
from UserStates import UserStates
from KeyBoard_helper import keyboards
import UserStorage

import PariService as ps

from to import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    UserStorage.save_user(message.from_user.username, message.chat.id)
    kb = keyboards[UserStates.BASE]
    await message.answer("Привет! Я пари-бот", reply_markup=kb)
    await state.set_state(UserStates.BASE)

@dp.message(F.text == "Мои пари", StateFilter(UserStates.BASE))
async def my_paris(message: types.Message):
    text = "Твои пари:"
    paris = ps.get_paris(message.from_user.id)
    for pari in paris:
        text +="\n" + pari
    await message.answer(text)

@dp.message(F.text == "Создать пари", StateFilter(UserStates.BASE))
async def add_pari(message: types.Message, state: FSMContext):
    text = ps.set_pari_name()
    await message.answer(text)
    await state.set_state(UserStates.CREATING_PARI)

@dp.message(StateFilter(UserStates.CREATING_PARI))
async def set_pari_name(message: types.Message, state: FSMContext):
    text = ps.set_pari_taker()
    await message.answer(text)
    await state.set_state(UserStates.SETTING_PARI_TAKEN)

@dp.message(StateFilter(UserStates.CREATING_PARI))
async def created_pari(message: types.Message, state: FSMContext):
    text = ps.pari_created()
    await message.answer(text)
    await state.set_state(UserStates.BASE)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

