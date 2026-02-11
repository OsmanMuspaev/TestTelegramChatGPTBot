# Telegram ChatGPT Bot

Telegram-бот на aiogram 3 с интеграцией OpenAI (ChatGPT) и поддержкой контекста диалога.


# Возможности

 - Общение с ChatGPT в Telegram
 - Запоминание контекста диалога
 - Очистка контекста командой /start или кнопкой «Новый запрос»
 - Готов к масштабированию

# Требования

 - Python 3.10+
 - OpenAI API Key

# Установка

Клонируй проект
```
git clone <your-repo-url>
cd <project-folder>
```

# Создай виртуальное окружение (рекомендуется)

## Linux / macOS
```
python3 -m venv venv
source venv/bin/activate
```

## Windows
```
python -m venv venv
venv\Scripts\activate
```

# Установи зависимости

```
pip install -r requirements.txt
```

Переменные окружения

Создай файл .env в корне проекта по шаблону который указан в файле .env.example:

```
TELEGRAM_BOT_TOKEN=8415775308:AAHQOe7tHGIU9KP1DJcchw9hTSq2dtBlDxk
OPENAI_API_KEY=твой_openai_api_key
```

# Конфигурация

Файл config.py:
``` python
GPT_MODEL = "gpt-4.1-mini"
```
При необходимости модель можно изменить в одном месте.


# Запуск бота

```
python bot.py
```
Если всё настроено правильно, бот начнёт polling и станет доступен в Telegram.


# Команды бота

 - /start - Очистка контекста и приветствие
 - /help - Инструкция по использованию
 - Новый запрос - Очистка контекста через кнопку


# Контекст диалога

 - История сообщений хранится в памяти
 - Контекст автоматически передаётся в ChatGPT
 - Контекст очищается:
     - командой /start
     - кнопкой «Новый запрос»