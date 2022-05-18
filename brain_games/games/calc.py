""" two functions for the Calculator Game!"""
from random import randint, choice

task_message = 'What is the result of the expression?'


def play_game():
    random_number_1, random_number_2 = randint(1, 100), randint(1, 100)
    random_operator = choice(["+", "-", "*"])
    game_question = (f'{str(random_number_1)} '
                     f'{str(random_operator)} '
                     f'{str(random_number_2)}')

    def count_random_result(number1, number2, number3):
        if number3 == "+":
            return number1 + number2
        elif number3 == "-":
            return number1 - number2
        elif number3 == "*":
            return number1 * number2
        else:
            return None

    right_answer = str(count_random_result(random_number_1,
                                           random_number_2,
                                           random_operator))
    return game_question, right_answer
