"""
    File name: NumberGame.py
    Author: Adam Kanoun
    Python Version: 3.9
"""
import random


class NumberGame:
    """
    A class representing the internal workings of the number memory game.
    === Public Attributes ===
    points: The number of answers the user has gotten correct.
    curr_num: The current number displayed on screen.
    lower_bound: The smallest number that should be tested this round.
    time_on_screen: The amount of time that the number will be displayed on
        screen (in seconds).
    begin: Represents whether or not the game has begun.

    === Representation Invariants ===
    points > 0
    lower_bound >= 1
    lower_bound  must be a multiple of 10
    time_on_screen > 0
    """
    points: int = 0
    curr_num: str
    lower_bound: int = 1
    time_on_screen: float = 1.7
    begin: bool = False

    def __init__(self) -> None:
        """
        Initialize the NumberGame class
        """
        pass

    def setup(self) -> None:
        """
        Sets up a NumberGame
        """
        self.points = 0
        self.lower_bound = 1
        self.assign_number_string()
        self.time_on_screen = 1.7
        self.begin = False

    def assign_number_string(self) -> None:
        """
        Create a number of length points + 1 digits and assigns it to
        curr_num.
        """
        self.curr_num = \
            str(random.randint(self.lower_bound, (self.lower_bound * 10) - 1))
        self.lower_bound *= 10

    def is_correct(self, answer: str) -> bool:
        """
        Checks to see whether or not the answer given is correct.
        """
        if answer == self.curr_num:
            return True
        return False

    def answer(self, answer: str) -> None:
        """
        What to do when answer is inputted.
        """
        if self.is_correct(answer):
            self.points += 1
            self.assign_number_string()
            self.time_on_screen += 0.2
        else:
            self.setup()
