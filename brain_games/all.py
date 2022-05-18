""" start_game - common engine for all games
    NUMBER_OF_GAMES - you can define max games for user session (3 by default)
"""
import prompt


def start_game(game_module):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_module.task_message)

    NUMBER_OF_GAMES: int = 3    # max games for user session

    for _ in range(NUMBER_OF_GAMES):
        game_question, right_answer = game_module.play_game()
        print(f'Question: {game_question}')
        user_answer = input(str('Your answer: '))
        if user_answer != right_answer:
            print(f"""\'{user_answer}\' is wrong answer ;(.
                Correct answer was \'{right_answer}\'.""")
            print(f"Let's try again, {user_name}!")
            break
        else:
            print('Correct!')
    else:
        print(f"Congratulations, {user_name}!")
