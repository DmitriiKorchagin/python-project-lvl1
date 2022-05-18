#!/usr/bin/env python3
""" the Brain Game Progression Script """
from brain_games.all import start_game
import brain_games.games.progression as game_module


def main():
    start_game(game_module)


if __name__ == '__main__':
    main()
