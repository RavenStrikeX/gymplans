# === Stage 9: Сортировка записей ===
# Project: GymPlans
def sort_exercises(records, by="name", reverse=False):
    """Сортирует список записей упражнения по названию или дате создания."""
    return sorted(records, key=lambda rec: rec[by], reverse=reverse)


def sort_by_name(records, reverse=False):
    """Сортировка по названию упражнения (поле 'name')."""
    return sort_exercises(records, by="name", reverse=reverse)


def sort_by_date(records, reverse=False):
    """Сортировка по дате создания (поле 'created_at')."""
    return sort_exercises(records, by="created_at", reverse=reverse)


def sort_records(records, by="name", reverse=False):
    """Универсальная сортировка записей упражнения.

    by: ключ сортировки ('name' или 'created_at').
    reverse: порядок (False - возрастание, True - убывание).
    """
    if by not in ("name", "created_at"):
        raise ValueError("Неверный ключ сортировки")
    return sort_exercises(records, by=by, reverse=reverse)
