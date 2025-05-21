# /* FifteenPuzzle.py

import pygame

from data.classes.Square import Square

class FifteenPuzzle:
    def __init__(self, display: pygame.surface.Surface, width: float, height: float):
        self.display = display
        self.width = width
        self.height = height
        self.vertical_squares = 4
        self.horizontal_squares = 4
        self.square_width = width // self.horizontal_squares
        self.square_height = height // self.vertical_squares
        self.selected_square: Square = None
        self.solved_values = [1,  2,  3,  4,
                              5,  6,  7,  8,
                              9,  10, 11, 12,
                              13, 14, 15, None]
        self.squares: list[Square] = self.generate_squares(self.solved_values)

    def generate_squares(self, initial_values: list[int | None]) -> list[Square]:
        output: list[Square] = []
        for y in range(self.vertical_squares):
            for x in range(self.horizontal_squares):
                index = y*self.horizontal_squares + x
                output.append(
                    Square(initial_values[index], index, x,  y, self.square_width, self.square_height)
                )
        return output
    
    def set_squares(self, values: list[int | None]) -> bool:
        if len(values) == len(self.squares):
            for i in range(len(self.squares)):
                self.squares[i].value = values[i]
                self.squares[i].unhighlight()
            return True
        return False
    
    def highlight(self):
        for i in range(len(self.squares)):
            self.squares[i].highlight()

    def get_square_from_pos(self, pos: tuple[float, float]) -> Square:
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
            
    def get_square_neighbors(self, square: Square) -> list[Square]:
        output: list[Square] = []
        # Try to add down, up, right, and left neighbors
        if (square.index + self.horizontal_squares) < len(self.squares):
            output.append(self.squares[square.index + self.horizontal_squares])
        if (square.index - self.horizontal_squares) >= 0:
            output.append(self.squares[square.index - self.horizontal_squares])
        if (square.index + 1) < len(self.squares):
            output.append(self.squares[square.index + 1])
        if (square.index - 1) >= 0:
            output.append(self.squares[square.index - 1])
        return output

    def handle_move(self, from_square: Square) -> bool:
        if from_square is not None:
            neighbors = self.get_square_neighbors(from_square)
            for neighbor in neighbors:
                if neighbor.value is None:
                    neighbor.value = from_square.value
                    from_square.value = None
                    return True
        return False
    
    def is_solved(self) -> bool:
        for i in range(len(self.squares)):
            if self.squares[i].value != self.solved_values[i]:
                return False
        return True

    def draw(self, display: pygame.surface.Surface = None):
        if display == None:
            display = self.display
        display.fill('white')
        for square in self.squares:
            square.draw(display)
        pygame.display.update()