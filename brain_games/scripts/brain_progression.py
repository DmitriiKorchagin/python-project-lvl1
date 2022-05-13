#!/usr/bin/env python3
""" the Brain Game Progression Script """
from ..games.all import start_game, welcome_user
from ..games.progression import play_progression


def main():
    pass


user_name = welcome_user()
print('What number is missing in the progression?')
start_game(play_progression, user_name)


if __name__ == '__main__':
    main()
