#!/usr/bin/env python3
""" two functions for the Even Number Game!"""
from random import randint


def is_even_number(num):
    """function defines even number and returns True or False """
    if num % 2 == 0:
        return True
    else:
        return False


def play_even():
    """ function define is user's answer correct about prime number """
    random_number = randint(1, 100)
    game_question = f'Question: {str(random_number)}'
    if is_even_number(random_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_question, right_answer
