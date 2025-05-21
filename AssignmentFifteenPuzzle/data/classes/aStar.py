import heapq
import pygame

from data.classes.FifteenPuzzle import FifteenPuzzle
from data.classes.Square import Square

#Arun Murugan
#CS 256
#3/19/2025
#Program that implements A* Search

#h-score: the number of misplaced tiles by comparing the current state and the goal state
#g-score: the number of nodes traversed from start node to get to the current node.
class AStarNode:
    def __init__(self, puzzle_state, parent=None, move=None, g=0, h=0):
        #create values for state of board
        #g_score, h_score, f_score
        #h_score will compare goal board with misplaced tiles in current board
        #current state of board
        #previous board
        #move made
        self.puzzle_state = puzzle_state
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = self.g + self.h

    #need to define to avoid typeerror for heap
    def __lt__(self, other):
        # compare f score of boards
        return self.f < other.f

#a search
class AStarAlgorithm:
    def __init__(self, board: FifteenPuzzle):
        self.board = board
        self.goal = self.board.solved_values
        self.moves = ['up', 'down', 'left', 'right']

    def misplaced_tiles(self, state) -> int:
        misplaced = 0
        for i in range(len(state)):
            value = state[i]
            if value is None:
                continue
            if value != self.goal[i]:
                misplaced += 1
        return misplaced

    #helper function, takes in given board 
        # find all boards using given board 
        # new list of boards
            # find the empty position in board
            # check neighbors up down left right if in bounds
            # make new board with empty pos and neighbor values swapped
            # store each board in list
        #return list of boards
    def generate_neighbors(self, current_board: list[int | None]) -> list[tuple]:
        neighbors = []
        empty_pos = current_board.index(None)
        x = empty_pos // 4
        y = empty_pos % 4
        # print("cell ", empty_pos, x, y)

        moves = [(0, -1, 'up'), (0, 1, 'down'), (-1, 0, 'left'), (1, 0, 'right')]

        for dx, dy, direction in moves:
            new_x, new_y = x + dx, y + dy

            # print("new x, new y ", new_x, new_y)

            if 0 <= new_x < 4 and 0 <= new_y < 4:
                new_pos = (new_x * 4)+ new_y
                # print("new pos ", new_pos)

                new_board = current_board.copy()
                new_board[empty_pos], new_board[new_pos] = new_board[new_pos], new_board[empty_pos]

                # print(new_board)

                neighbors.append((new_board, direction))
        
        return neighbors
    
    #given a board, check if board is solved board
    #if solved board, return all boards that got to solved board
    #if not solved board
        # store current board in a list of seen boards
        # call function to return all boards using current board
        # store the boards in a heap based on their f_score
        # take the min board
    def solve(self, start_state):
        open_list = []
        visited = set()

        start_node = AStarNode(start_state, g=0, h=self.misplaced_tiles(start_state))
        print("start node ", start_node)

        heapq.heappush(open_list, start_node)

        while open_list:
            current_node = heapq.heappop(open_list)
            print("current node ", current_node)

            # print("Current node properties:")
            print("Puzzle state:", current_node.puzzle_state)
            # print("g (cost so far):", current_node.g)
            # print("h (heuristic value):", current_node.h)
            # print("f (total cost):", current_node.f)
            # # print("Parent node:", current_node.parent)
            # print("Move from parent:", current_node.move)

            if current_node.puzzle_state == self.goal:
                path = []
                while current_node.parent is not None:
                    path.append(current_node.move)
                    current_node = current_node.parent
                return path[::-1]

            visited.add(tuple(current_node.puzzle_state))
            # print(visited)

            neighbors = self.generate_neighbors(current_node.puzzle_state)
            for neighbor, move in neighbors:
                if tuple(neighbor) in visited:
                    continue

                g = current_node.g + 1
                h = self.misplaced_tiles(neighbor)
                new_neighbor = AStarNode(neighbor, parent=current_node, move=move, g=g, h=h)
                print(new_neighbor.puzzle_state)
            
                heapq.heappush(open_list, new_neighbor)


