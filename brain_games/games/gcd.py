#!/usr/bin/env python3
""" two functions for the Great Devisor Game!"""
from random import randint
from .all import number_of_games
import prompt


def number_gcd(num1, num2):
    """ this function returns the greates common devisor between 2 numbers)"""
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def play_gcd(user_name):
    print('Find the greatest common divisor of given numbers.')
    user_count_answers = 0
    while user_count_answers < number_of_games:
        random_number_1 = randint(1, 100)
        random_number_2 = randint(1, 100)
        random_string = str(random_number_1) + " " + str(random_number_2)
        print('Question: ' + random_string)
        user_answer = prompt.integer('Your answer: ')
        right_answer = number_gcd(random_number_1, random_number_2)
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
