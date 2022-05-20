""" two functions for the Prime Number Game!"""
from random import randint
from math import sqrt

TASK_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_result_of_game():
    random_number = randint(2, 100)
    game_question = str(random_number)

    if is_prime_number(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_question, right_answer
