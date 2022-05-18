""" two functions for the Great Devisor Game!"""
from random import randint

task_message = 'Find the greatest common divisor of given numbers.'


def play_game():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)

    def is_gcd_number(number1, number2):
        while number1 != 0 and number2 != 0:
            if number1 > number2:
                number1 = number1 % number2
            else:
                number2 = number2 % number1
        return number1 + number2

    game_question = str(random_number_1) + " " + str(random_number_2)
    right_answer = str(is_gcd_number(random_number_1, random_number_2))
    return game_question, right_answer
