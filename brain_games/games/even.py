""" two functions for the Even Number Game!"""
from random import randint


task_message = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    """ function define is user's answer correct about prime number """
    random_number = randint(1, 100)
    game_question = str(random_number)
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_question, right_answer
