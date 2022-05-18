""" two functions for the Prime Number Game!"""
from random import randint
from math import sqrt

task_message = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_game():
    random_number = randint(2, 100)
    game_question = str(random_number)

    def is_prime_number(number):
        if number < 2:
            return False
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    if is_prime_number(random_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_question, right_answer
