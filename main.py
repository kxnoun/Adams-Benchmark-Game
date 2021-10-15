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
DARK_BROWN = (101, 67, 33)


class Screen:
    """
    The main screen for the game.
    === Representation Invariants ===
        Exactly one of the following attributes may be True at a time.
        intro_running, main_running, reaction_running, number_running,
        verbal_running.
    # TODO: Complete DOCSTRING
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
    reaction_buttons: List[Button]
    number_buttons: List[Button]
    verbal_buttons: List[Button]

    # INITIALIZER
    def __init__(self) -> None:
        """
        Initialize the Screen.
        """
        # Set up pygame
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Create the lists
        self.main_menu_buttons = []
        self.reaction_buttons = []
        self.number_buttons = []
        self.verbal_buttons = []

        # Create and append all the buttons
        self.create_main_menu_buttons()
        self.create_reaction_buttons()
        self.create_number_buttons()
        self.create_verbal_buttons()

        # Update/Flip the display.
        pygame.display.flip()

    # Create all the buttons
    def create_main_menu_buttons(self) -> None:
        """
        Creates the main menu's buttons.
        """
        # Create main_menu's buttons
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
        back_button = Button(BLACK, 15, 20, 100, 30, 20, "BACK", WHITE, WHITE)

        # Append main_menu's buttons
        self.main_menu_buttons.append(reaction_time_button)
        self.main_menu_buttons.append(number_memory_button)
        self.main_menu_buttons.append(verbal_memory_button)
        self.main_menu_buttons.append(back_button)

    def create_reaction_buttons(self) -> None:
        """
        Creates the reaction game's buttons.
        """
        reaction_button = Button(LIGHT_BROWN,
                                 (self.SCREEN_WIDTH / 2) - 500,
                                 (self.SCREEN_HEIGHT / 4), 1000, 500, 45,
                                 "Click to Begin!", DARK_BROWN, DARK_BROWN)
        back_button = Button(BLACK, 15, 20, 100, 30, 20, "BACK", WHITE, WHITE)
        self.reaction_buttons.append(back_button)
        self.reaction_buttons.append(reaction_button)

    def create_number_buttons(self) -> None:
        """
        Creates the number game's buttons
        """
        back_button = Button(BLACK, 15, 20, 100, 30, 20, "BACK", WHITE, WHITE)
        self.number_buttons.append(back_button)

    def create_verbal_buttons(self) -> None:
        """
        Creates the verbal game's buttons
        """
        back_button = Button(BLACK, 15, 20, 100, 30, 20, "BACK", WHITE, WHITE)
        self.verbal_buttons.append(back_button)

    # Helpful methods.
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

    # Game Intro methods
    def draw_game_intro(self) -> None:
        """
        A helper method for game_intro.
        This method draws the text and background for the game intro.
        """
        intro_font = pygame.font.Font('freesansbold.ttf', 100)
        sub_font = pygame.font.Font('freesansbold.ttf', 35)
        text, text_rect = self.text_obj("Adam's Benchmark Tests", BLACK,
                                        intro_font)
        subtext, subtext_rect = self.text_obj("Press Any Key to Begin", GREY,
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
                    else:
                        self.intro_running = False
                        self.main_running = True
                elif event.type == pygame.MOUSEBUTTONDOWN or \
                        event.type == pygame.MOUSEWHEEL:
                    self.intro_running = False
                    self.main_running = True
                if event.type == pygame.QUIT:
                    self.intro_running = False
                    self.game_running = False

    # Main Menu methods
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

    def main_menu_button_event_handler(self) -> None:
        """
        Precondition: the mouse is hovering over <button> on the main menu.
        A helper for draw_main_menu_buttons
        """
        for button in self.main_menu_buttons:
            if button.is_hover(pygame.mouse.get_pos()):
                self.main_running = False
                if button.text == "Reaction Time":
                    self.reaction_running = True
                elif button.text == "Number Memory":
                    self.number_running = True
                elif button.text == "Verbal Memory":
                    self.verbal_running = True
                elif button.text == "BACK":
                    self.intro_running = True
                else:
                    # Something may be wrong, so stay on main menu.
                    self.main_running = True

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

    def main_menu(self) -> None:
        """
        Runs the main menu scene.
        """
        while self.main_running and self.game_running:
            self.draw_background()
            self.draw_main_menu_text()
            self.draw_main_menu_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.main_menu_button_event_handler()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_running = False
                        self.game_running = False
                if event.type == pygame.QUIT:
                    self.main_running = False
                    self.game_running = False

    # Reaction Game's methods
    def draw_reaction_text(self) -> None:
        """
        Draws the reaction game's text.
        """
        title_font = pygame.font.Font('freesansbold.ttf', 60)
        text, text_rect = self.text_obj("Reaction Time Test", BLACK,
                                        title_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), \
                           (self.SCREEN_HEIGHT / 12)
        desc_font = pygame.font.Font('freesansbold.ttf', 20)
        description = 'As soon as the screen changes color and you see the' \
                      ' word "Go!", click as fast as you can to find your' \
                      ' reaction speed.'
        desc_text, desc_rect = self.text_obj(description, DARK_BROWN,
                                             desc_font)
        desc_rect.center = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 6)
        self.screen.blit(text, text_rect)
        self.screen.blit(desc_text, desc_rect)

    def reaction_button_event_handler(self) -> None:
        """
        The event handler for the buttons of the reaction game.
        """
        for button in self.reaction_buttons:
            if button.is_hover(pygame.mouse.get_pos()):
                if button.text == "BACK":
                    self.reaction_running = False
                    self.main_running = True
                else:
                    # Something may be wrong, so stay on reaction game.
                    self.reaction_running = True

    def draw_reaction_buttons(self) -> None:
        """
        Draws the buttons required for the reaction game.
        """
        for button in self.reaction_buttons:
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

    def reaction_game(self) -> None:
        """
        Runs the reaction time benchmark/game.
        """
        while self.reaction_running and self.game_running:
            self.draw_background()
            self.draw_reaction_text()
            self.draw_reaction_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.reaction_button_event_handler()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.reaction_running = False
                        self.game_running = False
                if event.type == pygame.QUIT:
                    self.reaction_running = False
                    self.game_running = False

    # Number game's methods
    def draw_number_text(self) -> None:
        """
        Draws the number game's text.
        """
        title_font = pygame.font.Font('freesansbold.ttf', 60)
        text, text_rect = self.text_obj("Number Memory Test", BLACK,
                                        title_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), \
                           (self.SCREEN_HEIGHT / 12)
        desc_font = pygame.font.Font('freesansbold.ttf', 20)
        description = 'Try to remember as many digits as possible!' \
                      ' The numbers of digits increase at every level.'
        desc_text, desc_rect = self.text_obj(description, DARK_BROWN,
                                             desc_font)
        desc_rect.center = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 6)
        self.screen.blit(text, text_rect)
        self.screen.blit(desc_text, desc_rect)

    def number_button_event_handler(self) -> None:
        """
        The event handler for the buttons of the number game.
        """
        for button in self.number_buttons:
            if button.is_hover(pygame.mouse.get_pos()):
                if button.text == "BACK":
                    self.number_running = False
                    self.main_running = True
                else:
                    # Something may be wrong, so stay on reaction game.
                    self.number_running = True

    def draw_number_buttons(self) -> None:
        """
        Draws the buttons required for the number game.
        """
        for button in self.number_buttons:
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

    def number_game(self) -> None:
        """
        Runs the number memory benchmark/game.
        """
        while self.number_running and self.game_running:
            self.draw_background()
            self.draw_number_text()
            self.draw_number_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.number_button_event_handler()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.number_running = False
                        self.game_running = False
                if event.type == pygame.QUIT:
                    self.number_running = False
                    self.game_running = False

    # Verbal game's methods
    def draw_verbal_text(self) -> None:
        """
        Draws the verbal game's text.
        """
        title_font = pygame.font.Font('freesansbold.ttf', 60)
        text, text_rect = self.text_obj("Verbal Memory Test", BLACK,
                                        title_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), \
                           (self.SCREEN_HEIGHT / 12)
        desc_font = pygame.font.Font('freesansbold.ttf', 20)
        description = 'Words will be shown once at a time, if the word' \
                      ' has been shown, click "shown", and if not, click "new".'
        desc_text, desc_rect = self.text_obj(description, DARK_BROWN,
                                             desc_font)
        desc_rect.center = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 6)
        self.screen.blit(text, text_rect)
        self.screen.blit(desc_text, desc_rect)

    def verbal_button_event_handler(self) -> None:
        """
        The event handler for the buttons of the verbal game.
        """
        for button in self.verbal_buttons:
            if button.is_hover(pygame.mouse.get_pos()):
                if button.text == "BACK":
                    self.verbal_running = False
                    self.main_running = True
                else:
                    # Something may be wrong, so stay on reaction game.
                    self.verbal_running = True

    def draw_verbal_buttons(self) -> None:
        """
        Draws the buttons required for the verbal game.
        """
        for button in self.verbal_buttons:
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

    def verbal_game(self) -> None:
        """
        Runs the verbal memory benchmark/game.
        """
        while self.verbal_running and self.game_running:
            self.draw_background()
            self.draw_verbal_text()
            self.draw_verbal_buttons()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.verbal_button_event_handler()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.verbal_running = False
                        self.game_running = False
                if event.type == pygame.QUIT:
                    self.verbal_running = False
                    self.game_running = False

    # This method runs the entire game.
    def run_game(self) -> None:
        """
        Runs the game
        """
        while self.game_running:
            self.game_intro()
            self.main_menu()
            self.reaction_game()
            self.number_game()
            self.verbal_game()


# Here, we call the run_game method to run the program.
if __name__ == '__main__':
    screen = Screen()
    screen.run_game()
