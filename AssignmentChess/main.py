import argparse
import pygame
import time

from data.classes.ChessMatch import chess_match
from data.classes.agents.RandomPlayer import RandomPlayer
from data.classes.agents.HumanPlayer import HumanPlayer
from data.classes.agents.ChessAgent import ChessAgent
from data.classes.agents.MonteCarloAgent import MonteCarloAgent
from data.classes.Board import Board

def main():
    parser = argparse.ArgumentParser(description="Initialize players for the game.")
    parser.add_argument('white', type=str, help="Type of the white player")
    parser.add_argument('black', type=str, help="type of the black player")
    args = parser.parse_args()
    print(args)
    if args.white not in globals().keys():
        print(f'White player {args.white} not found!')
        return
    if args.black not in globals().keys():
        print(f'Black player {args.black} not found!')
        return
    white_player: ChessAgent = globals()[args.white]('white')
    black_player: ChessAgent = globals()[args.black]('black')

    white_player_two: ChessAgent = globals()[args.black]('white')
    black_player_two: ChessAgent = globals()[args.white]('black')

    start_time = time.time()
    chess_match(white_player, black_player)
    end_time = time.time()
    print("duration of game: ", f"{end_time - start_time: .2f}", "seconds")

if __name__ == '__main__':
    main()