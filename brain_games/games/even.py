""" functions for the Even Number Game!"""
from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer_of_game():
    random_number = randint(1, 100)
    game_question = str(random_number)
    right_answer = 'no'
    if random_number % 2 == 0:
        right_answer = 'yes'
    return game_question, right_answer
