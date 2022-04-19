#!/usr/bin/env python3
""" the Brain Game Progression Script """
from ..games.all import welcome_user
from ..games.progression import play_progression


def main():
    print()


user_name = welcome_user()
play_progression(user_name)


if __name__ == '__main__':
    main()
