""" this module contains common functions and variables for all games:
    welcome_user - welcomes user if the right name as a string accepted
    number_of_games - max games for user session for all games (3 by default)
"""
import prompt


def welcome_user():
    """ funcion welcomes user, return his name"""
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


number_of_games: int = 3
