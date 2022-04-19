#!/usr/bin/env python3
""" two functions for the Prime Number Game!"""
from random import randint
from .all import number_of_games


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


def play_prime(user_name):    # noqa
    """ function define is user's answer correct about prime number """
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    user_count_answers = 0
    while user_count_answers < number_of_games:
        random_number = randint(2, 100)
        print('Question: ' + str(random_number))
        user_answer = input(str('Your answer: '))
        right_answer = is_prime_number(random_number)
        if right_answer is True and user_answer == 'yes':
            user_count_answers += 1
            print('Correct!')
        elif right_answer is False and user_answer == 'no':
            user_count_answers += 1
            print('Correct!')
        else:
            if user_answer == "yes":
                print('"yes" is wrong answer ;(. Correct answer was "no".')
            elif user_answer == "no":
                print('"no" is wrong answer ;(. Correct answer was "yes".')
            print(f'Let\'s try again, {user_name}!!')
            break
    if user_count_answers == 3:
        print(f'Congratulations, {user_name}!!')
