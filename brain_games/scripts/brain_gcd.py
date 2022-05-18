#!/usr/bin/env python3
""" the Brain Game Great Common Devisor Script """
from brain_games.all import start_game
import brain_games.games.gcd as game_module


def main():
    start_game(game_module)


if __name__ == '__main__':
    main()
