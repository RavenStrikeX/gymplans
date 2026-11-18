# === Stage 5: Связанная сущность ===
# Project: GymPlans
class Exercise:
    def __init__(self, name, muscle_group, weight, repetitions):
        self.id = None
        self.name = name
        self.muscle_group = muscle_group
        self.weight = weight
        self.repetitions = repetitions

    def set_id(self, exercise_id):
        self.id = exercise_id

    def __str__(self):
        return f"Упражнение #{self.id}: {self.name} ({self.muscle_group}, {self.weight} кг, {self.repetitions} повт.)"


class Approach:
    def __init__(self, exercise_id, sets, weight, repetitions):
        self.id = None
        self.exercise_id = exercise_id
        self.sets = sets
        self.weight = weight
        self.repetitions = repetitions

    def set_id(self, approach_id):
        self.id = approach_id

    def __str__(self):
        return (f"Подход #{self.id}: упражнение #{self.exercise_id}, "
                f"{self.sets} подходов, {self.weight} кг, {self.repetitions} повт.")


def add_exercise(exercise_id, name, muscle_group, weight, repetitions):
    exercise = Exercise(name, muscle_group, weight, repetitions)
    exercise.set_id(exercise_id)
    return exercise


def add_approach(approach_id, exercise_id, sets, weight, repetitions):
    approach = Approach(exercise_id, sets, weight, repetitions)
    approach.set_id(approach_id)
    return approach
