#!/usr/bin/env python3
""" two functions for the Great Devisor Game!"""
from random import randint


def number_gcd(num1, num2):
    """ this function returns the greates common devisor between 2 numbers)"""
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def play_gcd():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    random_string = str(random_number_1) + " " + str(random_number_2)
    game_question = f'Question: {random_string}'
    right_answer = str(number_gcd(random_number_1, random_number_2))
    return game_question, right_answer
