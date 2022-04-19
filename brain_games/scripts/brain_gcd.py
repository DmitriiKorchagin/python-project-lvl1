#!/usr/bin/env python3
""" the Brain Game Great Common Devisor Script """
from ..games.all import welcome_user
from ..games.gcd import play_gcd


def main():
    print()


user_name = welcome_user()
play_gcd(user_name)


if __name__ == '__main__':
    main()
