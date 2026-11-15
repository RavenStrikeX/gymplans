# === Stage 4: Редактирование записей ===
# Project: GymPlans
import re

ALLOWED_EXERCISE_FIELDS = {"name", "muscle_group", "weight", "reps"}


def _sanitize_value(field, value):
    if field == "name":
        value = str(value).strip()
        if not value:
            raise ValueError("Название не может быть пустым")
        value = re.sub(r"\s+", " ", value)
        return value
    if field == "muscle_group":
        value = str(value).strip()
        if not value:
            raise ValueError("Группа мышц не может быть пустой")
        return value
    if field in ("weight", "reps"):
        try:
            return float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Поле {field} должно быть числом")
    raise ValueError(f"Недопустимое поле: {field}")


def is_valid_update_payload(payload):
    if not isinstance(payload, dict):
        return False
    return bool(set(payload.keys()) <= ALLOWED_EXERCISE_FIELDS)


def validate_exercise_update(payload):
    if not is_valid_update_payload(payload):
        raise ValueError("Пayload содержит недопустимые поля")
    for field, value in payload.items():
        _sanitize_value(field, value)


def edit_exercise_by_id(exercise_id, payload):
    """Редактирует упражнения по id, применяя только допустимые поля."""
    if not isinstance(exercise_id, int) or exercise_id <= 0:
        raise ValueError("Некорректный идентификатор упражнения")
    if not is_valid_update_payload(payload):
        raise ValueError("Пayload содержит недопустимые поля")
    validate_exercise_update(payload)
    return exercise_id, payload
