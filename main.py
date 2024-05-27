from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StateFilter
from UserStates import UserStates
from KeyBoard_helper import get_keyboard

from to import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    kb = get_keyboard(["/test"])
    await message.answer("Привет! Я пари-бот", reply_markup=kb)
    await state.set_state(UserStates.BASE)

@dp.message(Command("test"), StateFilter(UserStates.BASE))
async def start(message: types.Message):
    await message.answer("Ты в состоянии BASE")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

