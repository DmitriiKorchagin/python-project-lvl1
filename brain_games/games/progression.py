""" functions for the Ariphmetic Progression Game!"""
from random import randint

RULES = 'What number is missing in the progression?'


def get_question_and_answer():
    current_number = randint(1, 50)
    difference_number = randint(1, 50)
    progression_numbers = []
    progression_numbers.append(str(current_number))
    for i in range(1, 10):
        current_number += difference_number
        progression_numbers.append(str(current_number))
    random_missing_number_index = randint(0, 9)
    right_answer = progression_numbers[random_missing_number_index]
    progression_numbers[random_missing_number_index] = ".."
    game_question = " ".join(progression_numbers)
    return game_question, right_answer
