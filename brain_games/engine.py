""" run - common engine for all games
    NUMBER_OF_ROUNDS - you can define max game's rounds (3 by default)
"""
import prompt


NUMBER_OF_ROUNDS: int = 3    # max game's rounds for user session


def run(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULES)

    for _ in range(NUMBER_OF_ROUNDS):
        game_question, right_answer = game.get_question_and_answer_of_game()
        print(f'Question: {game_question}')
        user_answer = input(str('Your answer: '))
        if user_answer != right_answer:
            print(f"""\'{user_answer}\' is wrong answer ;(.
                Correct answer was \'{right_answer}\'.""")
            print(f"Let's try again, {user_name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {user_name}!")
