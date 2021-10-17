"""
    File name: ReactionGame.py
    Author: Adam Kanoun
    Python Version: 3.9
"""
import random


class ReactionGame:
    """
    A class representing the reaction game's inner workings.
    === Public Attributes ===
    start: Represents if the game has started or not, specifically, when the
        user first clicks to launch the game.
    wait_time: Represents the interval of time (in seconds) between the
        "wait" time and "go" time.
    failed: Represents whether or not the user clicked too early, if they did
        the user failed this attempt.
    reaction_speed: Represents the interval of time (in seconds) between the
        "go" time and the "click".

    === Representation Invariants ===
    wait_time > 1
    reaction_speed > 0
    """
    start: bool = False
    wait_time: int
    failed: bool = False
    reaction_speed: float

    def __init__(self) -> None:
        """
        Initialize ReactionGame
        """
        pass

    def setup(self) -> None:
        """
        Set up a reaction game.
        """
        self.start = False
        self.failed = False
        self.generate_wait_time()

    def generate_wait_time(self) -> None:
        """
        Generate a random wait time.
        """
        self.wait_time = random.randint(1, 5)
