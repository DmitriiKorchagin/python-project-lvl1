#!/usr/bin/env python3
""" the Brain Game Prime Number Script """
from ..games.all import start_game, welcome_user
from ..games.prime import play_prime


def main():
    pass


user_name = welcome_user()
print('Answer "yes" if given number is prime. Otherwise answer "no".')
start_game(play_prime, user_name)


if __name__ == '__main__':
    main()
