""" welcome_user - return user's name
    start_game - common engine for all games
    number_of_games - max games for user session for all games (3 by default)
"""
import prompt

number_of_games: int = 3


def welcome_user():
    """ funcion welcomes user, return his name"""
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def start_game(func_game, user_name):
    user_count_answers = 0
    while user_count_answers < number_of_games:
        game_question, right_answer = func_game()
        print(game_question)
        user_answer = input(str('Your answer: '))
        if user_answer == right_answer:
            user_count_answers += 1
            print('Correct!')
        else:
            print(f"""\'{user_answer}\' is wrong answer ;(.
                Correct answer was \'{right_answer}\'.""")
            print(f"Let's try again, {user_name}!")
            break
    if user_count_answers == number_of_games:
        print(f"Congratulations, {user_name}!")
