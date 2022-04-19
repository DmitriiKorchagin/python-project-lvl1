#!/usr/bin/env python3
""" the Brain Even Game Script """
from ..games.all import welcome_user
from ..games.even import play_even


def main():
    print()


user_name = welcome_user()
play_even(user_name)


if __name__ == '__main__':
    main()
