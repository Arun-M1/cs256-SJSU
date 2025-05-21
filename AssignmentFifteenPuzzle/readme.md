## Assignment Description
Your task is to implement the A* algorithm for finding the solution to the Fifteen Puzzle. Each node in the graph to be searched by A* will be a puzzle configuration. You may place your implementation `.py` file in `data/classes/`. You must collect data on the performance of your agent (running time, number of steps to get to the solution) across at least 10 different initial configurations. Refer to the lecture slides for examples of heuristics for this kind of puzzle.

## Setup Instructions
You can install the requirements (only pygame) by running `pip install -r requirements.txt`

Then you can run the program with `python main.py --human` to solve the puzzle yourself by clicking on the squares you want to move into the empty space. `python main.py --a-star` should run your implementation and evaluation of performance.

## Game Details
When you are solving the puzzle as a human, if you get the puzzle into the goal configuration, then all the squares will turn green and the text `Player solved!` will be printed in the terminal. Otherwise, `Player did not solve` will be printed.

As a human player, you can click on any square adjacent (no diagonals) to the empty square to move that number into the empty square.