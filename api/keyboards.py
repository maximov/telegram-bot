from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="История сообщений")],
        [KeyboardButton(text="ℹПомощь")]
    ],
    resize_keyboard=True
)
