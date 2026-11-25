# === Stage 8: Фильтрация записей ===
# Project: GymPlans
from datetime import date


def filter_exercises_by_group(exercises, group):
    result = []
    for exercise in exercises:
        if getattr(exercise, "group", None) == group:
            result.append(exercise)
    return result


def filter_exercises_by_date_range(exercises, start_date, end_date):
    result = []
    for exercise in exercises:
        date_value = getattr(exercise, "date", None)
        if isinstance(date_value, date):
            if start_date is None or end_date is None:
                if date_value >= start_date and date_value <= end_date:
                    result.append(exercise)
            else:
                result.append(exercise)
    return result


def filter_exercises(exercises, group=None, start_date=None, end_date=None):
    filtered_by_group = filter_exercises_by_group(exercises, group)
    filtered_by_date = filter_exercises_by_date_range(filtered_by_group, start_date, end_date)
    return filtered_by_date


if __name__ == "__main__":
    class Exercise:
        def __init__(self, name, group, weight, reps, date=None):
            self.name = name
            self.group = group
            self.weight = weight
            self.reps = reps
            self.date = date

        def __repr__(self):
            return f"Exercise(name={self.name}, group={self.group}, weight={self.weight}, reps={self.reps}, date={self.date})"

    sample_exercises = [
        Exercise("Приседания", "Ноги", 80, 10, date(2023, 1, 15)),
        Exercise("Жим лежа", "Грудь", 60, 8, date(2023, 2, 20)),
        Exercise("Становая тяга", "Спина", 100, 5, date(2023, 3, 10)),
        Exercise("Подтягивания", "Спина", 0, 12, date(2023, 4, 5)),
    ]

    filtered = filter_exercises(sample_exercises, group="Спина", start_date=date(2023, 1, 1), end_date=date(2023, 12, 31))
    for item in filtered:
        print(item)
