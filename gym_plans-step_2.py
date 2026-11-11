# === Stage 2: Проверка полей ===
# Project: GymPlans
from typing import Any


def normalize_name(name: str) -> str:
    return " ".join(name.strip().split()).title()


def normalize_group(group: str) -> str:
    return " ".join(group.strip().lower().split())


def normalize_int(value: Any, default: int) -> int:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default


def validate_exercise(data: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []

    name = normalize_name(data.get("name", ""))
    if not name:
        errors.append("Название упражнения не может быть пустым")
    else:
        data["name"] = name

    group = normalize_group(data.get("group", ""))
    if not group:
        errors.append("Укажите группу мышц")
    else:
        data["group"] = group

    weight = normalize_int(data.get("weight", 0), 0)
    if weight < 0:
        errors.append("Вес не может быть отрицательным")
    else:
        data["weight"] = weight

    reps = normalize_int(data.get("reps", 0), 0)
    if reps < 0:
        errors.append("Число повторений не может быть отрицательным")
    else:
        data["reps"] = reps

    return data, errors
