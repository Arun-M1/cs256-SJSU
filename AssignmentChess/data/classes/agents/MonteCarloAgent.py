import random
from typing import List, Tuple, Literal
import math
import copy
import time
from collections import defaultdict

from data.classes.agents.ChessAgent import ChessAgent
from data.classes.Square import Square
from data.classes.Board import Board

class MCNode:
    def __init__(self, board: Board, parent: None, move: Tuple[Square, Square] = None):
        #board, parent board, children (can be list or set), possible moves that have not been used, # wins for board, # visits for board
        self.board = board
        self.parent = parent
        self.children = []
        # self.untried_moves = self.get_possible_moves()
        self.wins = 0
        self.visits = 0
        self.move = move
        self.depth = 0

    #generate all moves from current board
    def get_possible_moves(self) -> List[Tuple[Square, Square]]:
        possible_moves = []
        for square in self.board.squares:
            #check if there is a piece on the square and if the piece belongs to agent
            if square.occupying_piece and square.occupying_piece.color == self.board.turn:
                #get valid moves for piece
                valid_moves = square.occupying_piece.get_valid_moves(self.board)
                #for each move, generate tuple of position and move
                for mv in valid_moves:
                    possible_moves.append((square, mv))
                
        return possible_moves
    
    # def is_fully_expanded(self):
    #     return len(self.get_possible_moves()) == 0

    #figure out which board (child) gives the best score, UCB
    def best_child(self, exploration_constant = 0.5) -> 'MCNode':
        max_ucb = float('-inf')
        best_child = None

        for child in self.children:
            #start, children have 0 visits so 0 divison is undefined
            if child.visits == 0:
                cur_ucb = float('inf')
            else:
                exploitation_term = child.wins / child.visits #exploitation
                exploration_term = exploration_constant * math.sqrt((math.log(self.visits)) / child.visits) #exploration
                cur_ucb = exploitation_term + exploration_term
        
            if cur_ucb > max_ucb:
                max_ucb = cur_ucb
                best_child = child

        return best_child

class MonteCarloAgent(ChessAgent):
    def __init__(self, color: Literal['white', 'black']):
        super().__init__(color)
        #limit same move choice to 3
        self.board_history = defaultdict(int)
    
    def choose_action(self, board: Board):
        start_time = time.time()
        best_child_node = self.mcts(board)
        end_time = time.time()

        print(f"{end_time - start_time: .2f} seconds")

        hash_board_state = best_child_node.board.get_hash_board()
        move = best_child_node.move
        #board has been seen 3 times already
        if hash_board_state in self.board_history and self.board_history[hash_board_state] > 2:
            print("board has been seen 3 times")
            return False
        self.board_history[hash_board_state] += 1
        return move

    def mcts(self, root: Board):
        root_node = MCNode(root, None)

        #select best child node from root board
        best_child_node = self.selection(root_node)
        # print(f"best child node {best_child_node}")

        #expand on best child node
        self.expand(best_child_node)
        if best_child_node:
            #for each new child from best child node
            for child in best_child_node.children:
                #run simulation on each new child
                res, last_sim_node = self.simulation(child)

                #backpropogate from last simulation node to best child node
                self.backpropogate(last_sim_node, res)
        
        #found the best child node of the root, return it
        best_node = root_node.best_child()

        return best_node

    def make_children(self, node: MCNode):
        untried_moves = []

        if node:
            untried_moves = node.get_possible_moves()

        if not untried_moves:
            return node

        while untried_moves:
            current_move = untried_moves.pop()
            #apply the move
            new_board = copy.deepcopy(node.board)

            from_square_pos = current_move[0]
            to_square_pos = current_move[1]
            from_square_pos_new = new_board.get_square_from_pos((from_square_pos.x, from_square_pos.y))
            to_square_pos_new = new_board.get_square_from_pos((to_square_pos.x, to_square_pos.y))

            if not (new_board.apply_move(from_square_pos_new, to_square_pos_new)):
                print("failed to apply move, invalid")

            child_node = MCNode(new_board, parent=node, move=current_move)

            node.children.append(child_node)
        
    def selection(self, node: MCNode) -> MCNode: #return best child
        #while there are untried moves for root node, make children nodes and add to children list
        self.make_children(node)

        best_child = node.best_child()

        #go through children and pick out the best one, return best one
        return best_child

    #create all leaves for the given leaf node and append to children of leaf node
    def expand(self, node: MCNode):
        self.make_children(node)

    #simulate the game from current node to end, return if board is in checkmate state
    def simulation(self, node: MCNode) -> Tuple[int, MCNode]:
        move_count = 0
        sim_board_history = defaultdict(int)
        current_board = node.board
        current_node = node
        color = current_board.turn

        #while the current board is not in checkmate state for either player
        while not current_board.is_in_checkmate(color):
            possible_moves = []

            # Generate all possible moves from the current board state
            for square in current_board.squares:
                if square.occupying_piece and square.occupying_piece.color == color:
                    # Get valid moves for each piece
                    valid_moves = square.occupying_piece.get_valid_moves(current_board)
                    for mv in valid_moves:
                        # print(square.occupying_piece.pos, mv.pos)
                        possible_moves.append((square, mv))

            if not possible_moves: #draw
                # print(f"return draw, no possible moves")
                break

            if move_count > 50: #enforce move limit
                break
            
            #get random move
            new_move = random.choice(possible_moves)

            #check for board state existing
            hash_board = current_board.get_hash_board()
            if hash_board in sim_board_history and sim_board_history[hash_board] > 2:
                # print(f"board appears in history 3 times")
                break
            sim_board_history[hash_board] += 1

            #apply random move to board
            current_board.handle_move(new_move[0], new_move[1])
            new_child_node = MCNode(current_board, parent=current_node, move=new_move)
            new_child_node.depth = current_node.depth + 1

            #switch color turn
            color = "black" if color == "white" else "white"

            current_node = new_child_node
            if current_node.depth > 4: #can set limit of simulations depth
                # print(f"depth exceeds max depth {current_node.depth}")
                break
            move_count += 1
        
        #if board in checkmate, return 
        if current_node.board.is_in_checkmate("white"):
            # print("checkmate white")
            return -1, current_node
        if current_node.board.is_in_checkmate("black"):
            # print("checkmate black")
            return 1, current_node
        
        return 0, current_node

    #backpropagation, update scores of new children for leaf node until leaf node
    def backpropogate(self, node: MCNode, result: int):
        current_node = node
        #exit when it hits leaf node
        while current_node is not None:
            current_node.visits += 1
            #check if color is agent's color
            if current_node.board.turn == self.color:
            #check if won
                if result == 1:
                    current_node.wins += 1
            #otherwise lost
            else:
                if result == -1:
                    current_node.wins -= 1

            #go to parent node of child node
            current_node = current_node.parent