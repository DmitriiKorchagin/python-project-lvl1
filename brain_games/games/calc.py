""" two functions for the Calculator Game!"""
from random import randint, choice

TASK_MESSAGE = 'What is the result of the expression?'


def get_result_of_game():
    random_number_1, random_number_2 = randint(1, 100), randint(1, 100)
    random_operator = choice(["+", "-", "*"])
    game_question = (f'{str(random_number_1)} '
                     f'{str(random_operator)} '
                     f'{str(random_number_2)}')
    if random_operator == "+":
        right_answer = str(random_number_1 + random_number_2)
    elif random_operator == "-":
        right_answer = str(random_number_1 - random_number_2)
    elif random_operator == "*":
        right_answer = str(random_number_1 * random_number_2)
    return game_question, right_answer
