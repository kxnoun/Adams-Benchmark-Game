"""
    File name: Screen.py
    Author: Adam Kanoun
    Python Version: 3.9
"""
import pygame
import time
from typing import Tuple, List
from Button import Button
from ReactionGame import ReactionGame
from NumberGame import NumberGame
from VerbalGame import VerbalGame

# COLOR CONSTANTS
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
DARK_GREY = (105, 105, 105)
LIGHT_YELLOW = (255, 255, 158)
LIGHT_BROWN = (196, 164, 132)
DARK_BROWN = (101, 67, 33)
DARK_BLUE = (20, 52, 164)
JADE = (0, 163, 108)
ALT_RED = (245, 31, 10)
ORANGE = (255, 165, 0)

# FONTS
SANS_FONT = 'freesansbold.ttf'


class Screen:
    """
    The main screen for the game.

    === Public Attributes ===
    SCREEN_WIDTH: The width of the screen in pixels.
    SCREEN_HEIGHT: The height of the screen in pixels.
    BACKGROUND: The color of the background in RBG.
    screen: The display of the game.
    game_running: A boolean representing whether or not the main game loop is
        running.
    intro_running: A boolean representing whether or not the game introduction
        scene is running.
    main_running: A boolean representing whether or not the main menu screen
        is running.
    reaction_running: A boolean representing whether or not the reaction game
        is running.
    number_running: A boolean representing whether or not the number game
        is running.
    verbal_running: A boolean representing whether or not the verbal game
        is running.
    main_menu_buttons: A list of all the buttons in the main menu.
    reaction_buttons: A list of all the buttons in the reaction game.
    number_buttons: A list of all the buttons in the number game.
    verbal_buttons: A list of all the buttons in the verbal game.
    words: An attribute that runs the VerbalGame class and has vital attributes
        and methods for the verbal game to work.
    clicked_textbox: Represents whether the text box in the verbal game has
        been clicked.
    textbox: Represents the text box in the verbal game.
    numbers: An attribute that runs the NumberGame class and has vital
        attributes and methods for the number game to work.
    can_type: Represents whether or not the user can type on the textbox.
    react: An attribute that runs the ReactGame class and has vital attributes
        and methods for the react game to work.
    react_button: Represents the main button in the reaction game.

    === Private Attributes ===
    _start_time: Used in both the number game and the reaction game, this
        attribute represents a necessary start time. For the number game, this
        is used to calculate how long the displayed number should be shown.
        For the reaction game, this is used to calculate everything after
        the first click to start the game.

    === Representation Invariants ===
        Exactly one of the following attributes may be True at a time.
        intro_running, main_running, reaction_running, number_running,
        verbal_running.

        SCREEN_WIDTH, SCREEN_HEIGHT > 0
        _start_time >= 0
    """
    SCREEN_WIDTH: int = 1280
    SCREEN_HEIGHT: int = 720
    screen: pygame.Surface
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
    words: VerbalGame = VerbalGame()
    clicked_textbox: bool = False
    textbox: Button
    numbers: NumberGame = NumberGame()
    _start_time: float = 0
    can_type: bool = True
    react: ReactionGame = ReactionGame()
    react_button: Button

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
        self.react_button = reaction_button
        self.reaction_buttons.append(back_button)
        self.reaction_buttons.append(reaction_button)

    def create_number_buttons(self) -> None:
        """
        Creates the number game's buttons
        """
        input_rect = Button(WHITE, self.SCREEN_WIDTH / 2 - 600,
                            self.SCREEN_HEIGHT / 1.5, 1200, 100, 40,
                            'Write "start" and press enter to begin!',
                            DARK_GREY)
        back_button = Button(BLACK, 15, 20, 100, 30, 20, "BACK", WHITE, WHITE)
        self.textbox = input_rect
        self.number_buttons.append(back_button)
        self.number_buttons.append(input_rect)

    def create_verbal_buttons(self) -> None:
        """
        Creates the verbal game's buttons
        """
        shown_button = Button(DARK_BLUE, self.SCREEN_WIDTH / 13,
                              self.SCREEN_HEIGHT / 1.7, 225, 75, 30, "Shown",
                              WHITE, WHITE)
        new_button = Button(JADE, self.SCREEN_WIDTH / 13,
                            self.SCREEN_HEIGHT / 3, 225, 75, 30,
                            "New", WHITE, WHITE)
        back_button = Button(BLACK, 15, 20, 100, 30, 20, "BACK", WHITE, WHITE)
        self.verbal_buttons.append(back_button)
        self.verbal_buttons.append(shown_button)
        self.verbal_buttons.append(new_button)

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
        intro_font = pygame.font.Font(SANS_FONT, 100)
        sub_font = pygame.font.Font(SANS_FONT, 35)
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
        main_menu_font = pygame.font.Font(SANS_FONT, 60)
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
        title_font = pygame.font.Font(SANS_FONT, 60)
        text, text_rect = self.text_obj("Reaction Time Test", BLACK,
                                        title_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), \
                           (self.SCREEN_HEIGHT / 12)
        desc_font = pygame.font.Font(SANS_FONT, 20)
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
                elif button == self.react_button:
                    if self.react.start is False and self.react.failed:
                        self.react.setup()
                    elif self.react.start is False:
                        self.react_button.color = ALT_RED
                        self.react_button.outline = RED
                        self.react_button.text_color = WHITE
                        self.react_button.font_size = 70
                        self.react_button.text = "Wait!"
                        self.react.start = True
                        self._start_time = time.time()
                    elif time.time() - self._start_time < self.react.wait_time:
                        self.react.failed = True
                        self.react.start = False
                    elif time.time() - self._start_time > self.react.wait_time:
                        self.react.reaction_speed = time.time() - \
                                                    self._start_time - \
                                                    self.react.wait_time
                        self.react_button.text = \
                            str(int(self.react.reaction_speed * 1000)) + " ms"
                        self.react.start = False
                else:
                    # Something may be wrong, so stay on reaction game.
                    self.reaction_running = True

    def draw_reaction_buttons(self) -> None:
        """
        Draws the buttons required for the reaction game.
        """
        for button in self.reaction_buttons:
            if time.time() - self._start_time >= self.react.wait_time and \
                    self.react.start:
                if button == self.react_button:
                    self.react_button.color = JADE
                    self.react_button.text = "GO!"
                    self.react_button.outline = GREEN
            elif self.react.failed is True:
                self.react_button.text = "Woah! Try again!"
                self.react_button.color = ORANGE
                self.react_button.outline = ORANGE
                self.react_button.text_color = RED
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
        self.react.setup()
        self.react_button.text = "Click to Begin!"
        self.react_button.font_size = 45
        self.react_button.outline = DARK_BROWN
        self.react_button.color = LIGHT_BROWN
        self.react_button.text_color = DARK_BROWN
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
        title_font = pygame.font.Font(SANS_FONT, 60)
        text, text_rect = self.text_obj("Number Memory Test", BLACK,
                                        title_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), \
                           (self.SCREEN_HEIGHT / 12)
        desc_font = pygame.font.Font(SANS_FONT, 20)
        description = 'Try to remember as many digits as possible!' \
                      ' The numbers of digits increase at every level.'
        desc_text, desc_rect = self.text_obj(description, DARK_BROWN,
                                             desc_font)
        desc_rect.center = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 6)
        if self.numbers.begin is True:
            point_text, point_rect = self.text_obj("Score", ALT_RED, title_font)
            point_rect.center = \
                (self.SCREEN_WIDTH / 1.19, self.SCREEN_HEIGHT / 4)
            pygame.draw.line(self.screen, ALT_RED,
                             (self.SCREEN_WIDTH / 1.3,
                              self.SCREEN_HEIGHT / 3.4),
                             (self.SCREEN_WIDTH / 1.1,
                              self.SCREEN_HEIGHT / 3.4),
                             3)
            num_font = pygame.font.Font(SANS_FONT, 70)
            num_text, num_rect = self.text_obj(str(self.numbers.points),
                                               ALT_RED, num_font)
            num_rect.center = \
                (self.SCREEN_WIDTH / 1.19, self.SCREEN_HEIGHT / 2.7)
            self.screen.blit(point_text, point_rect)
            self.screen.blit(num_text, num_rect)
        if time.time() - self._start_time < self.numbers.time_on_screen:
            self.can_type = False
            number_font = pygame.font.Font(SANS_FONT, 60)
            number, number_rect = \
                self.text_obj(self.numbers.curr_num, BLACK, number_font)
            number_rect.center = \
                (self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2)
            self.screen.blit(number, number_rect)
        else:
            self.can_type = True
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
                elif button == self.textbox:
                    self.textbox.outline = BLUE
                    self.clicked_textbox = True
                    self.textbox.font_size = 50
                    self.textbox.text = ""
                    self.textbox.text_color = BLACK
                else:
                    # Something may be wrong, so stay on reaction game.
                    self.number_running = True
            else:
                if self.clicked_textbox is False \
                        and self.numbers.begin is False:
                    self.textbox.text_color = DARK_GREY
                    self.textbox.font_size = 40
                    self.textbox.text = \
                        'Write "start" and press enter to begin!'
                elif self.clicked_textbox is False and self.numbers.begin:
                    self.textbox.text_color = DARK_GREY
                    self.textbox.font_size = 40
                    self.textbox.text = \
                        'Write the number here!'
                self.clicked_textbox = False

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
            if button.color == WHITE and \
                    button.is_hover(pygame.mouse.get_pos()):
                button.outline = BLUE
            elif button.color == WHITE and self.clicked_textbox is False:
                button.outline = None
            button.draw(self.screen)
            button.color = orig_button_color

    def number_game(self) -> None:
        """
        Runs the number memory benchmark/game.
        """
        self.numbers.setup()
        self._start_time = 0
        self.textbox.text_color = DARK_GREY
        self.textbox.font_size = 40
        self.textbox.text = 'Write "start" and press enter to begin!'
        self.clicked_textbox = False
        self.can_type = True
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
                    elif event.key == pygame.K_BACKSPACE and \
                            self.clicked_textbox:
                        self.textbox.text = self.textbox.text[:-1]
                    elif event.key == pygame.K_RETURN and self.clicked_textbox \
                            and self.numbers.begin is False:
                        if self.textbox.text.lower() == "start":
                            self._start_time = time.time()
                            self.textbox.text = ""
                            self.numbers.begin = True
                            self.can_type = False
                    elif event.key == pygame.K_RETURN and self.clicked_textbox \
                            and self.numbers.begin is True:
                        if self.textbox.text.strip().isnumeric():
                            temp = self.textbox.text
                            if self.numbers.is_correct(
                                    self.textbox.text.strip()):
                                self._start_time = time.time()
                                self.textbox.text = ""
                            else:
                                self._start_time = 0
                                self.textbox.text_color = DARK_GREY
                                self.textbox.font_size = 40
                                self.clicked_textbox = False
                                self.textbox.text = \
                                    'Click again and write "start"'
                                self.can_type = True
                            self.numbers.answer(temp.strip())
                    else:
                        if self.clicked_textbox and self.can_type:
                            self.textbox.text += event.unicode
                if event.type == pygame.QUIT:
                    self.number_running = False
                    self.game_running = False

    # Verbal game's methods
    def draw_verbal_text(self) -> None:
        """
        Draws the verbal game's text.
        """
        title_font = pygame.font.Font(SANS_FONT, 60)
        text, text_rect = self.text_obj("Verbal Memory Test", BLACK,
                                        title_font)
        text_rect.center = (self.SCREEN_WIDTH / 2), \
                           (self.SCREEN_HEIGHT / 12)
        desc_font = pygame.font.Font(SANS_FONT, 20)
        description = 'Words will be shown once at a time, if the word' \
                      ' has been shown, click "shown", and if not, click "new".'
        desc_text, desc_rect = self.text_obj(description, DARK_BROWN,
                                             desc_font)
        desc_rect.center = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 6)
        word_font = pygame.font.Font(SANS_FONT, 60)
        word_text, word_rect = self.text_obj(self.words.curr_word, BLACK,
                                             word_font)
        word_rect.center = (self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)
        point_text, point_rect = self.text_obj("Score", ALT_RED, word_font)
        point_rect.center = (self.SCREEN_WIDTH / 1.19, self.SCREEN_HEIGHT / 3.2)
        pygame.draw.line(self.screen, ALT_RED,
                         (self.SCREEN_WIDTH / 1.3, self.SCREEN_HEIGHT / 2.83),
                         (self.SCREEN_WIDTH / 1.1, self.SCREEN_HEIGHT / 2.83),
                         3)
        num_font = pygame.font.Font(SANS_FONT, 70)
        num_text, num_rect = self.text_obj(str(self.words.points), ALT_RED,
                                           num_font)
        num_rect.center = (self.SCREEN_WIDTH / 1.19, self.SCREEN_HEIGHT / 2.1)
        self.screen.blit(text, text_rect)
        self.screen.blit(desc_text, desc_rect)
        self.screen.blit(word_text, word_rect)
        self.screen.blit(point_text, point_rect)
        self.screen.blit(num_text, num_rect)

    def verbal_button_event_handler(self) -> None:
        """
        The event handler for the buttons of the verbal game.
        """
        for button in self.verbal_buttons:
            if button.is_hover(pygame.mouse.get_pos()):
                if button.text == "BACK":
                    self.verbal_running = False
                    self.main_running = True
                elif button.text == "New" or button.text == "Shown":
                    self.words.answer(button.text)
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
        self.words.setup()
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
