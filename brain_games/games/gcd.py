""" functions for the Great Devisor Game!"""
from random import randint

GAME_RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd_number(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2


def get_question_and_answer_of_game():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    game_question = str(random_number_1) + " " + str(random_number_2)
    right_answer = str(get_gcd_number(random_number_1, random_number_2))
    return game_question, right_answer
