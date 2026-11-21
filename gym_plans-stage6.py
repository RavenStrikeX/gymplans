# === Stage 6: Связи между сущностями ===
# Project: GymPlans
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional


@dataclass
class Exercise:
    name: str
    muscle_group: str
    weight: float
    reps: int


@dataclass
class Approach:
    exercise: Exercise
    weight: float
    reps: int


class GymPlansIntegrity:
    """Работа с подходами для упражнения и проверка целостности связей."""

    def get_all_approaches(self, approaches_by_exercise: Dict[str, List[Approach]],
                           exercise_name: str) -> List[Approach]:
        """Возвращает все подходы для заданного упражнения по имени."""
        return list(approaches_by_exercise.get(exercise_name, []))

    def validate_relationship(self, approaches: List[Approach],
                              exercise_name: str) -> Tuple[bool, List[str]]:
        """
        Проверяет целостность связей между упражнениями и подходами.

        Проверяет:
        1. Все подходы принадлежат упражнению с соответствующим названием.
        2. Веса и повторения в подходе не меньше, чем в упражнении.
        """
        errors: List[str] = []

        for approach in approaches:
            if approach.exercise.name != exercise_name:
                errors.append(
                    f"Подход '{approach.exercise.name}' не соответствует "
                    f"запрошенному упражнению '{exercise_name}'"
                )
            if approach.weight < approach.exercise.weight:
                errors.append(
                    f"Вес в подходе ({approach.weight}) меньше веса в "
                    f"упражнении ({approach.exercise.weight})"
                )
            if approach.reps < approach.exercise.reps:
                errors.append(
                    f"Повторения в подходе ({approach.reps}) меньше "
                    f"повторений в упражнении ({approach.exercise.reps})"
                )

        return (len(errors) == 0, errors)

    def build_approaches_map(self, exercises: List[Exercise],
                             approaches: List[Approach]) -> Dict[str, List[Approach]]:
        """Строит карту подходов по имени упражнения."""
        map_approaches: Dict[str, List[Approach]] = {}
        for approach in approaches:
            map_approaches.setdefault(approach.exercise.name, []).append(approach)
        return map_approaches
