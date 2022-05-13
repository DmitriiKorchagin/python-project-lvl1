#!/usr/bin/env python3
""" two functions for the Calculator Game!"""
from random import randint


def random_result(num1, num2, num3):
    """ this function returns the result
    of +, - or * between num1 and num2
    (num3 is operator 1: +, 2: -, 3: *)"""
    if num3 == 1:
        return num1 + num2
    elif num3 == 2:
        return num1 - num2
    elif num3 == 3:
        return num1 * num2
    else:
        return None


def play_calc():
    random_list = [0, "+", "-", "*"]
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    random_action = randint(1, 3)
    random_string = (f'{str(random_number_1)} '
                     f'{str(random_list[random_action])} '
                     f'{str(random_number_2)}')
    game_question = f'Question: {random_string}'
    right_answer = str(random_result(random_number_1,
                                     random_number_2,
                                     random_action))
    return game_question, right_answer
