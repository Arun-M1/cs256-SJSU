## Assignment
Arun Murugan
CS 256
Assignment 5

## Code Description
Code implements a chess AI agent that utilizes Monte Carlo Tree Search to choose the best move against its opponent. MCNode is a class that represents a node in the MCTS tree for the chess game for the agent, taking in the board and attributes to determine its best child node and what moves the node has from its current state. 

Agent has a main MCTS function that executes the 4 main steps of Monte Carlo, then figures out the best child node to take from the parent node (board). It also maintains history of past boards to determine the game state is draw by threefold repetition. First it will select the best child node. Then it will expand on that child node and create the children for that child node. Then it runs simulations on the newly created children to reach end conditions: Win, Loss, Draw. Finally, it backpropogates, updating the scores of children using UCB formula. Once the 4 steps are complete, it will choose the best move to take next. 

## Setup Instructions
You can install the requirements (only pygame) by running `pip install -r requirements.txt`

Then you can run the program with `python3 hundred_matches_script.py` to have the agent play against the randomplayer. Every iteration of the script will swap sides for the players so there is variance in the games. 


