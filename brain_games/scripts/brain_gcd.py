#!/usr/bin/env python3
""" the Brain Game Great Common Devisor Script """
from ..games.all import start_game, welcome_user
from ..games.gcd import play_gcd


def main():
    pass


user_name = welcome_user()
print('Find the greatest common divisor of given numbers.')
start_game(play_gcd, user_name)


if __name__ == '__main__':
    main()
