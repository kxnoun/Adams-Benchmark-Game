"""
    File name: Button.py
    Author: Adam Kanoun
    Python Version: 3.9
"""
from typing import Tuple, Optional, Union
import pygame


class Button:
    """
    A class representing a button in pygame.
    # TODO: Complete Docstring
    """
    text: str
    text_color: Tuple[int, int, int]
    font_size: int
    color: Tuple[int, int, int]
    x: Union[int, float]
    y: Union[int, float]
    width: Union[int, float]
    height: Union[int, float]

    def __init__(self, color: Tuple[int, int, int], x: Union[int, float],
                 y: Union[int, float], width: Union[int, float],
                 height: Union[int, float], font_size: int, text: str = "",
                 text_color: Tuple[int, int, int] = (0, 0, 0),
                 outline: Optional[Tuple[int, int, int]] = None) -> None:
        """
        Initialize a button.
        """
        self.text = text
        self.text_color = text_color
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.outline = outline

    def draw_button(self, screen: pygame.Surface) -> None:
        """
        Draw a button on the screen.
        """
        if self.outline is not None:
            # Draw a rectangle with color <outline> that is bigger than width
            # and height, to make it seem like it is an outline.
            pygame.draw.rect(screen, self.outline, (self.x - 2, self.y - 2,
                                               self.width + 4,
                                               self.height + 4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width,
                                              self.height), 0)

    def draw_text(self, screen: pygame.Surface) -> None:
        """
        Draw the text for the button.
        """
        if self.text != '':
            button_font = pygame.font.Font('freesansbold.ttf', self.font_size)
            text = button_font.render(self.text, True, self.text_color)
            text_rect = text.get_rect()
            text_rect.center = ((self.x + (self.width / 2)), self.y +
                                (self.height / 2))
            screen.blit(text, text_rect)

    def draw(self, screen: pygame.Surface) -> None:
        self.draw_button(screen)
        self.draw_text(screen)

    def is_hover(self, position: Tuple[int, int]) -> bool:
        """
        Returns whether or not the mouse is hovering over the button (when the
        mouse is at <position> (x, y)).
        """
        if self.x < position[0] < self.x + self.width and \
                self.y < position[1] < self.y + self.height:
            return True
        return False
