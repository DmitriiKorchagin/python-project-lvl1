""" functions for the Prime Number Game!"""
from random import randint
from math import sqrt

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    random_number = randint(2, 100)
    game_question = str(random_number)
    right_answer = 'no'
    if is_prime(random_number):
        right_answer = 'yes'
    return game_question, right_answer
