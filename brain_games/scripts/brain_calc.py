#!/usr/bin/env python3
""" the Brain Game Calculator Script """
from ..games.all import welcome_user
from ..games.calc import play_calc


def main():
    print()


user_name = welcome_user()
play_calc(user_name)


if __name__ == '__main__':
    main()
