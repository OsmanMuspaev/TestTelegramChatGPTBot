import logging
from aiogram import Router, types

from services.chatgpt import generate_answer
from storage.dialog import get_history, clear_history

router = Router()


@router.message(lambda msg: msg.text == "Новый запрос")
async def new_dialog(message: types.Message):
    clear_history(message.from_user.id)
    await message.answer("Контекст очищен. Задавай новый вопрос")

@router.message()
async def chat_handler(message: types.Message):
    history = get_history(message.from_user.id)

    history.append({
        "role": "user",
        "content": message.text
    })

    try:
        answer = await generate_answer(history)

        history.append({
            "role": "assistant",
            "content": answer
        })

        await message.answer(answer)
    
    except Exception as e:
        logging.exception("Ошибка при обращении к ChatGPT")
        await message.answer("Ошибка при обращении к ChatGPT")
