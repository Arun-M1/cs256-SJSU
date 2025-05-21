# /* PuzzleInstance.py

import pygame

from data.classes.FifteenPuzzle import FifteenPuzzle
from data.classes.HumanPlayer import HumanPlayer

def puzzle_instance(player: HumanPlayer, initial_values: list[int | None]):
    pygame.init()
    WINDOW_SIZE = (600, 600)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = FifteenPuzzle(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
    if not board.set_squares(initial_values):
        print("Invalid initial values!")
        return
    moves_count: int = 0

    # Run the main game loop
    running = True
    while running:
        chosen_action = player.choose_action(board)
        moves_count += 1
        if chosen_action == False or moves_count > 1000:
            print('Player did not solve')
            running = False
        elif board.is_solved():
            print('Player solved!')
            board.highlight()
            running = False
        board.draw()

    # Allow the player to view the result
    viewing = True
    while viewing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                viewing = False