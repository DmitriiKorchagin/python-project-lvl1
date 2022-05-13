#!/usr/bin/env python3
""" two functions for the Prime Number Game!"""
from random import randint


def is_prime_number(num):
    """ this function defines the prime number and returns True or False """
    if num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def play_prime():
    random_number = randint(2, 100)
    game_question = f'Question: {str(random_number)}'
    if is_prime_number(random_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_question, right_answer
