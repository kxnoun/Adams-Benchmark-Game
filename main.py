"""
Adam Kanoun
This is where the benchmark game runs!
"""
import pygame
from typing import Tuple, List
from Button import Button

# COLOR CONSTANTS
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
LIGHT_YELLOW = (255, 255, 158)
LIGHT_BROWN = (196, 164, 132)


class Screen:
    """
    The main screen for the game.
    """
    SCREEN_WIDTH: int = 1280
    SCREEN_HEIGHT: int = 720
    BACKGROUND: Tuple[int, int, int] = LIGHT_YELLOW
    game_running: bool = True
    intro_running: bool = True
    main_running: bool = False
    reaction_running: bool = False
    number_running: bool = False
    verbal_running: bool = False
    main_menu_buttons: List[Button]

    def __init__(self) -> None:
        """
        Initialize the Screen.
        === Representation Invariants ===
        Exactly one of the following attributes may be True at a time.
        intro_running, main_running, reaction_running, number_running,
        verbal_running.
        """
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        # Create buttons
        self.main_menu_buttons = []
        reaction_time_button = Button(LIGHT_BROWN,
                                      (self.SCREEN_WIDTH / 2) - 500,
                                      (self.SCREEN_HEIGHT / 3), 250, 250, 30,
                                      "Reaction Time", BLACK, BLACK)
        number_memory_button = Button(LIGHT_BROWN,
                                      (self.SCREEN_WIDTH / 2) - 125,
                                      self.SCREEN_HEIGHT / 3, 250, 250, 30,
                                      "Number Memory", BLACK, BLACK)
        verbal_memory_button = Button(LIGHT_BROWN,
                                      (self.SCREEN_WIDTH / 2) + 250,
                                      self.SCREEN_HEIGHT / 3, 250, 250, 30,
                                      "Verbal Memory", BLACK, BLACK)
        back_button1 = Button(BLACK, 15, 20, 100, 30, 20, "BACK", WHITE, WHITE)
        self.main_menu_buttons.append(reaction_time_button)
        self.main_menu_buttons.append(number_memory_button)
        self.main_menu_buttons.append(verbal_memory_button)
        self.main_menu_buttons.append(back_button1)
        pygame.display.flip()

    @staticmethod
    def text_obj(text: str, color: Tuple[int, int, int], font) -> Tuple:
        """
        Convert the string <text> into a text object in the game.
        """
        screen_text = font.render(text, True, color)
        return screen_text, screen_text.get_rect()

    def draw_background(self) -> None:
        """
        Simply draws the background color.
        """
        self.screen.fill(self.BACKGROUND)

    def draw_game_intro(self) -> None:
        """
        A helper method for game_intro.
        This method draws the text and background for the game intro.
        """
        intro_font = pygame.font.Font('freesansbold.ttf', 100)
        sub_font = pygame.font.Font('freesansbold.ttf', 35)
        text, text_rect = self.text_obj("Adam's Benchmark Tests", BLACK,
                                        intro_font)
        subtext, subtext_rect = self.text_obj("Press Space to Begin", GREY,
                                              sub_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2)
        subtext_rect.center = (self.SCREEN_WIDTH / 2), \
                              (2 * self.SCREEN_HEIGHT / 3)
        self.screen.blit(text, text_rect)
        self.screen.blit(subtext, subtext_rect)

    def game_intro(self) -> None:
        """
        Runs the opening scene.
        """
        while self.intro_running and self.game_running:
            self.draw_background()
            self.draw_game_intro()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.intro_running = False
                        self.game_running = False
                    elif event.key == pygame.K_SPACE:
                        self.intro_running = False
                if event.type == pygame.QUIT:
                    self.intro_running = False
                    self.game_running = False

    def draw_main_menu_text(self) -> None:
        """
        Draws the main menu text
        """
        main_menu_font = pygame.font.Font('freesansbold.ttf', 60)
        text, text_rect = self.text_obj("Choose any game!", BLACK,
                                        main_menu_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), \
                           (self.SCREEN_HEIGHT / 12)
        self.screen.blit(text, text_rect)

    def draw_main_menu_buttons(self) -> None:
        """
        Draws the main menu buttons.
        """
        for button in self.main_menu_buttons:
            orig_button_color = button.color
            if button.is_hover(pygame.mouse.get_pos()):
                button.color = (button.color[0] + (255 -
                                                   button.color[0]) * 0.3,
                                button.color[1] + (255 -
                                                   button.color[1]) * 0.3,
                                button.color[2] + (255 -
                                                   button.color[2]) * 0.3)
            button.draw(self.screen)
            button.color = orig_button_color

    def press_main_menu_button(self):
        pass

    def main_menu(self) -> None:
        """
        Runs the main menu scene.
        """
        self.main_running = True
        while self.main_running and self.game_running:
            self.draw_background()
            self.draw_main_menu_text()
            self.draw_main_menu_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                # Check mouse clicks and positions to determine if any
                # running attributes must be changed.
                # if self.reaction_running is True then run reaction_game
                # elif self.number_running is True then run number_game
                # elif self.verbal_running is True then run verbal_game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_running = False
                        self.game_running = False
                if event.type == pygame.QUIT:
                    self.main_running = False
                    self.game_running = False

        # Use assertion to make sure representation invariants are working as
        # they should.

    def reaction_game(self) -> None:
        """
        Runs the reaction time benchmark/game.
        """
        pass

    def number_game(self) -> None:
        """
        Runs the number memory benchmark/game.
        """
        pass

    def verbal_game(self) -> None:
        """
        Runs the verbal memory benchmark/game.
        """
        pass

    def run_game(self) -> None:
        """
        Runs the game
        """
        pass


if __name__ == '__main__':
    screen = Screen()
    screen.game_intro()
    screen.main_menu()
