#!/usr/bin/env python3
""" the Brain Game Calculator Script """
from ..games.all import start_game, welcome_user
from ..games.calc import play_calc


def main():
    pass


user_name = welcome_user()
print('What is the result of the expression?')
start_game(play_calc, user_name)


if __name__ == '__main__':
    main()
