from aiogram import Router, types
from aiogram.filters import Command
from db.repository import save_message

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я сохраняю все твои сообщения в базу.")

@router.message()
async def echo_handler(message: types.Message):
    await save_message(user_id=message.from_user.id, text=message.text)
    await message.answer(f"Я сохранил твоё сообщение: {message.text}")
