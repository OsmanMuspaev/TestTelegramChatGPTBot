from aiogram import Router, types
from aiogram.filters import Command

from keyboards.keyboards import main_keyboard
from storage.dialog import clear_history

router = Router()

# /start
@router.message(Command("start"))
async def start_handler(message: types.Message):
    clear_history(message.from_user.id)
    await message.answer(
        "Привет!\n"
        "Я Telegram-бот с ChatGPT.\n"
        "Контекст диалога сброшен.",
        reply_markup=main_keyboard
    )

# /help
@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(
        "Как пользоваться ботом:\n"
        " - Напиши любой текст — я отвечу\n"
        " - Я помню контекст диалога\n"
        " - /start или «Новый запрос» — очистка контекста"
    )