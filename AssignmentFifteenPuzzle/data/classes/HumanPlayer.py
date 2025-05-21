# /* HumanPlayer.py

import pygame

from data.classes.Square import Square
from data.classes.FifteenPuzzle import FifteenPuzzle

class HumanPlayer:

    def choose_action(self, board: FifteenPuzzle) -> Square | bool:
        choosing_move = True
        while choosing_move:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    x = mx // board.square_width
                    y = my // board.square_height
                    clicked_square = board.get_square_from_pos((x, y))
                    if board.handle_move(clicked_square):
                        return True
            board.draw()