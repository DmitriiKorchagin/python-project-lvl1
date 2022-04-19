#!/usr/bin/env python3
from random import randint
from .all import number_of_games


def is_even_number(num):
    """function defines even number and returns True or False """
    if num % 2 == 0:
        return True
    else:
        return False


def play_even(user_name):    # noqa
    """ function define is user's answer correct about prime number """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_count_answers = 0
    while user_count_answers < number_of_games:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        user_answer = input(str('Your answer: '))
        right_answer = is_even_number(random_number)
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
