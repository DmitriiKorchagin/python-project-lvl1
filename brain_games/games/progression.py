#!/usr/bin/env python3
""" two functions for the Ariphmetic Progression Game!"""
from random import randint
from .all import number_of_games
import prompt


def make_progression_line():
    """ this function returns the ariphmetic progression
    with randomly missing number)"""
    ran_num_1 = randint(1, 50)
    ran_num_2 = randint(1, 50)
    progression_list = []
    progression_list.append(ran_num_1)
    for i in range(1, 10):
        ran_num_1 += ran_num_2
        progression_list.append(ran_num_1)
    ran_num_3 = randint(1, 9)
    missing_number = progression_list[ran_num_3]
    progression_list[ran_num_3] = ".."
    progression_string = " ".join(map(str, progression_list))
    return progression_string, missing_number


def play_progression(user_name):
    print('What number is missing in the progression?')
    user_count_answers = 0
    while user_count_answers < number_of_games:
        (prog_string, right_answer) = make_progression_line()
        print('Question: ' + prog_string)
        user_answer = prompt.integer('Your answer: ')
        if user_answer == right_answer:
            user_count_answers += 1
            print('Correct!')
        else:
            print(f"""{str(user_answer)}\' is wrong answer ;(.
                Correct answer was '{str(right_answer)}'.""")
            print(f"Let's try again, {user_name}!")
            break
    if user_count_answers == 3:
        print(f"Congratulations, {user_name}!")
