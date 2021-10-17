"""
    File name: ReactionGame.py
    Author: Adam Kanoun
    Python Version: 3.9
"""
import random


class ReactionGame:
    """
    A class representing the reaction game.
    """
    start: bool = False
    wait_time: int
    failed: bool = False
    reaction_speed: float

    def __init__(self):
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
