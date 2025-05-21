import pygame
import time

from data.classes.ChessMatch import chess_match
from data.classes.agents.RandomPlayer import RandomPlayer
from data.classes.agents.HumanPlayer import HumanPlayer
from data.classes.agents.ChessAgent import ChessAgent
from data.classes.agents.MonteCarloAgent import MonteCarloAgent
from data.classes.Board import Board

def loop_one_hundred_times():
    arg1 = 'RandomPlayer'
    # arg1 = 'HumanPlayer'
    arg2 = 'MonteCarloAgent'

    white_player: ChessAgent = globals()[arg1]('white')
    # white_player = HumanPlayer('white')
    black_player: ChessAgent = globals()[arg2]('black')
    # black_player = MonteCarloAgent('black')

    white_player_two: ChessAgent = globals()[arg2]('white')
    # white_player_two = MonteCarloAgent('white')
    black_player_two: ChessAgent = globals()[arg1]('black')
    # black_player_two = HumanPlayer('black')

    for i in range(10):
        print("Game ", i + 1)
        if i % 2 == 0:
            # print("game white vs black")
            start_time = time.time()
            chess_match(white_player, black_player)
            end_time = time.time()
            print("duration of game: ", f"{end_time - start_time: .2f}", "seconds")
        else:
            # print("game white 2 vs black 2")
            start_time = time.time()
            chess_match(white_player_two, black_player_two)
            end_time = time.time()
            print("duration of game: ", f"{end_time - start_time: .2f}", "seconds")

if __name__ == "__main__":
    loop_one_hundred_times()