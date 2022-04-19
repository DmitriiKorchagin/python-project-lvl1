#!/usr/bin/env python3
""" two functions for the Calculator Game!"""
from random import randint
from .all import number_of_games
import prompt


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


def play_calc(user_name):
    random_list = [0, "+", "-", "*"]
    print('What is the result of the expression?')
    user_count_answers = 0
    while user_count_answers < number_of_games:
        random_number_1 = randint(1, 100)
        random_number_2 = randint(1, 100)
        random_action = randint(1, 3)
        random_string = (f'{str(random_number_1)} '
                         f'{str(random_list[random_action])} '
                         f'{str(random_number_2)}')
        print('Question: ' + random_string)
        user_answer = prompt.integer('Your answer: ')
        right_answer = random_result(random_number_1,
                                     random_number_2,
                                     random_action)
        if user_answer == right_answer:
            user_count_answers += 1
            print('Correct!')
        else:
            print(f"""'{str(user_answer)}\' is wrong answer ;(.
                Correct answer was '{str(right_answer)}'.""")
            print(f"Let's try again, {user_name}!")
            break
    if user_count_answers == 3:
        print(f"Congratulations, {user_name}!")
