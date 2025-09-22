from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="История сообщений")],
        [KeyboardButton(text="ℹПомощь")],
    ],
    resize_keyboard=True,
)
