from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keybord = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="start"),
            KeyboardButton(text="help")
        ],
        [
            KeyboardButton(text="menu"),
            KeyboardButton(text="all_commands")
        ],
        [
            KeyboardButton(text="verify your phone number",
                            request_contact=True)
        ]
    ],
    resize_keyboard=True
)