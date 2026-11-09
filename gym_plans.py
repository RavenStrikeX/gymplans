# === Stage 1: Каркас модуля ===
# Project: GymPlans
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Exercise:
    name: str
    muscle_group: str
    weight: Optional[float] = None
    reps: Optional[int] = None


def demo_exercises() -> List[Exercise]:
    return [
        Exercise(name="Жим штанги лежа", muscle_group="Грудь", weight=60.0, reps=10),
        Exercise(name="Становая тяга", muscle_group="Спина", weight=100.0, reps=5),
        Exercise(name="Приседания", muscle_group="Ноги", weight=80.0, reps=12),
        Exercise(name="Подтягивания", muscle_group="Руки", weight=None, reps=8),
    ]


def main() -> None:
    exercises = demo_exercises()
    print("Генератор тренировочных планов GymPlans")
    print("Доступные упражнения:")
    for exercise in exercises:
        weight_str = f"{exercise.weight:g} кг" if exercise.weight is not None else "собственный вес"
        reps_str = f"{exercise.reps} повт" if exercise.reps is not None else "по желанию"
        print(f"  - {exercise.name} [{exercise.muscle_group}]: {weight_str}, {reps_str}")
    print("Добро пожаловать в систему планирования тренировок!")


if __name__ == "__main__":
    main()
