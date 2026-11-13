# === Stage 3: Хранилище в памяти ===
# Project: GymPlans
from uuid import uuid4


class Exercise:
    def __init__(self, name, muscle_group, weight, repetitions):
        self.id = str(uuid4())
        self.name = name
        self.muscle_group = muscle_group
        self.weight = weight
        self.repetitions = repetitions


class ExerciseStore:
    def __init__(self):
        self._exercises = {}

    def add(self, name, muscle_group, weight, repetitions):
        exercise = Exercise(name, muscle_group, weight, repetitions)
        self._exercises[exercise.id] = exercise
        return exercise

    def get(self, exercise_id):
        return self._exercises.get(exercise_id)

    def list_all(self):
        return list(self._exercises.values())
