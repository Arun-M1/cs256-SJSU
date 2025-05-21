import argparse
import time

from data.classes.PuzzleInstance import puzzle_instance
from data.classes.HumanPlayer import HumanPlayer
from data.classes.FifteenPuzzle import FifteenPuzzle
from data.classes.aStar import AStarAlgorithm

def main():
    parser = argparse.ArgumentParser(description="Initialize player for the game.")
    parser.add_argument('--human', action='store_true', help="Used for human to play the puzzle")
    parser.add_argument('--a-star', action='store_true', help="Used for human to play the puzzle")
    args = parser.parse_args()
    if args.human:
        human_player = HumanPlayer()
        # Reversed Order
        # initial_values = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, None]
        # One move away from solved
        initial_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 15]
        puzzle_instance(human_player, initial_values)
    if args.a_star:
        print("IMPLEMENT A*")
        states = {
            "state_1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, None, 15],
            "state_2": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, 14, 15],
            "state_3": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, 13, 14, 15],
            "state_4": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None, 13, 14, 15, 12],
            "state_5": [1, 2, 3, 4, 5, 6, 7, None, 9, 10, 11, 8, 13, 14, 15, 12],
            "state_6": [1, 2, 3, None, 5, 6, 7, 4, 9, 10, 11, 8, 13, 14, 15, 12],
            "state_7": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None, 12, 13, 14, 11, 15],
            "state_8": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, None, 13, 14, 11, 15],
            "state_9":  [1, 2, 3, 4, None, 5, 7, 8, 9, 6, 10, 12, 13, 14, 11, 15],
            "state_10": [None, 2, 3, 4, 1, 5, 7, 8, 9, 6, 10, 12, 13, 14, 11, 15]
        }

        puzzle = FifteenPuzzle(display=None, width=600, height=600)
        for state, state_values in states.items():
            puzzle.set_squares(state_values)

            print("initial puzzle ", state_values)

            solver = AStarAlgorithm(puzzle)

            start_time = time.time()

            result = solver.solve(state_values)

            end_time = time.time()

            if result:
                print("Path found")
                print("time duration ", f"{end_time - start_time: .2f}", "seconds.")
                print("time duration ", end_time - start_time, "seconds.")
                print("number of steps ", len(result))

if __name__ == '__main__':
    main()