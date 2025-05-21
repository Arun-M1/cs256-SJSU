# /* Square.py

from __future__ import annotations
import pygame

class Square:
    def __init__(self, value: int | None, index: int, x: int, y: int, width: float, height: float):
        self.value = value
        self.index = index
        self.x = x
        self.y  = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)
        self.default_color = (180, 140, 255)
        self.highlight_color = (140, 200, 80)
        self.draw_color = self.default_color
        self.coord = self.get_coord()
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width-1,
            self.height-1
        )

    def get_coord(self) -> str:
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def highlight(self):
        self.draw_color = self.highlight_color

    def unhighlight(self):
        self.draw_color = self.default_color

    def draw(self, display: pygame.surface.Surface) -> None:
        pygame.draw.rect(display, self.draw_color, self.rect)
        # adds the chess piece icons
        if self.value != None:
            font = pygame.font.Font(None, 74)
            text_surface = font.render(str(self.value), True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            display.blit(text_surface, text_rect)