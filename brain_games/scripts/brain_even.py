#!/usr/bin/env python3
""" the Brain Even Game Script """
from ..games.all import start_game, welcome_user
from ..games.even import play_even


def main():
    pass


user_name = welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no".')
start_game(play_even, user_name)

if __name__ == '__main__':
    main()
