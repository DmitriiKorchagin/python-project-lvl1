#!/usr/bin/env python3
""" the Brain Game Prime Number Script """
from ..games.all import welcome_user
from ..games.prime import play_prime


def main():
    print()


user_name = welcome_user()
play_prime(user_name)


if __name__ == '__main__':
    main()
