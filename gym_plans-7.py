# === Stage 7: Генерация идентификаторов ===
# Project: GymPlans
import string
import secrets


PROJECT_PREFIX = "gymplan"


def generate_unique_id(prefix: str, counter: dict) -> str:
    """Генерация уникального идентификатора с префиксом и проверкой коллизий."""
    while True:
        unique_suffix = secrets.token_hex(4)
        candidate = f"{prefix}-{unique_suffix}"
        if candidate not in counter:
            counter[candidate] = 1
            return candidate


def generate_sequential_id(prefix: str, counter: dict, start: int = 1) -> str:
    """Генерация последовательного идентификатора с проверкой коллизий."""
    while True:
        candidate = f"{prefix}-{start}"
        if candidate not in counter:
            counter[candidate] = 1
            return candidate
        start += 1


def generate_alphanumeric_id(prefix: str, counter: dict) -> str:
    """Генерация идентификатора из букв и цифр с проверкой коллизий."""
    alphabet = string.ascii_letters + string.digits
    while True:
        unique_suffix = "".join(secrets.choice(alphabet) for _ in range(6))
        candidate = f"{prefix}-{unique_suffix}"
        if candidate not in counter:
            counter[candidate] = 1
            return candidate


if __name__ == "__main__":
    counter = {}
    id1 = generate_unique_id(PROJECT_PREFIX, counter)
    print(id1)
    id2 = generate_sequential_id(PROJECT_PREFIX, counter)
    print(id2)
    id3 = generate_alphanumeric_id(PROJECT_PREFIX, counter)
    print(id3)
