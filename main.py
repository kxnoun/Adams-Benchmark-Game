"""
Adam Kanoun
This is where the benchmark tests run!
"""
import pygame
from typing import Tuple

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
LIGHT_YELLOW = (255, 255, 158)


class Screen:
    """
    The main screen for the game.
    """
    SCREEN_WIDTH: int = 1280
    SCREEN_HEIGHT: int = 720
    BACKGROUND: Tuple[int, int, int] = LIGHT_YELLOW
    running: bool = True
    game_running: bool = True
    intro: bool = True

    def __init__(self) -> None:
        """
        Initialize the Screen.
        """
        # self.mouse_pos = (-1, 1)
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        pygame.display.flip()

    @staticmethod
    def text_obj(text: str, color: Tuple[int, int, int], font) -> Tuple:
        """
        Convert the string <text> into a text object in the game.
        """
        screen_text = font.render(text, True, color)
        return screen_text, screen_text.get_rect()

    def draw_window(self):
        """
        Draw the window
        """
        self.screen.fill(self.BACKGROUND)
        pygame.display.flip()

    def game_intro(self):
        """
        Draw the first home scene.
        """
        while self.intro:
            self.screen.fill(self.BACKGROUND)
            intro_font = pygame.font.Font('freesansbold.ttf', 100)
            sub_font = pygame.font.Font('freesansbold.ttf', 35)
            text, text_rect = self.text_obj("Adam's Benchmark Tests",
                                            BLACK, intro_font)
            subtext, subtext_rect = self.text_obj("Press Space to Begin", GREY,
                                                  sub_font)
            text_rect.center = (self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2)
            subtext_rect.center = (self.SCREEN_WIDTH / 2), \
                                  (2 * self.SCREEN_HEIGHT / 3)
            self.screen.blit(text, text_rect)
            self.screen.blit(subtext, subtext_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.intro = False
                        self.running = False
                    elif event.key == pygame.K_SPACE:
                        self.intro = False
                if event.type == pygame.QUIT:
                    self.intro = False
                    self.running = False

    def main(self):
        """
        The main loop of the code.
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw_window()


if __name__ == '__main__':
    screen = Screen()
    screen.game_intro()
    screen.main()
