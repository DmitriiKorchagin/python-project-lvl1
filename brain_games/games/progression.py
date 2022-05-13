#!/usr/bin/env python3
""" two functions for the Ariphmetic Progression Game!"""
from random import randint


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
    missing_number = str(progression_list[ran_num_3])
    progression_list[ran_num_3] = ".."
    progression_string = " ".join(map(str, progression_list))
    return progression_string, missing_number


def play_progression():
    (prog_string, right_answer) = make_progression_line()
    game_question = f'Question: {prog_string}'
    return game_question, right_answer
