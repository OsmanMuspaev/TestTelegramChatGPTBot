dialog_history: dict[int, list] = {}

# Получить историю чата
def get_history(user_id: int) -> list:
    return dialog_history.setdefault(user_id, [])

# Очистить историю чата
def clear_history(user_id: int):
    dialog_history[user_id] = []