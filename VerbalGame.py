"""
    File name: VerbalGame.py
    Author: Adam Kanoun
    Python Version: 3.9
"""

import random
from typing import List, Set, Optional


class VerbalGame:
    """
    A class representing the verbal game's inner workings.
    """
    words: List[str]
    game_words: List[str]
    words_shown: List[str]
    points: int = 0
    curr_word: str

    def __init__(self):
        self.load_random_words()

    def load_random_words(self) -> None:
        """
        From words.txt, load up all the words and shuffle them.
        """
        with open('words.txt') as word_file:
            self.words = word_file.read().split()
        random.shuffle(self.words)

    def get_1000_words(self) -> List:
        """
        Get any 1000 words from self.words.
        """
        a = random.randint(1, 360000)
        return self.words[a: a + 1000]

    def setup(self) -> None:
        """
        Set up a game.
        """
        self.points = 0
        self.words_shown = []
        self.game_words = self.get_1000_words()
        self.curr_word = self.game_words[self.points]

    def is_correct(self, answer: str) -> bool:
        """
        Check whether the answer inputted is correct.
        """
        if (answer == "New") and (self.curr_word not in self.words_shown):
            return True
        elif (answer == "Shown") and (self.curr_word in self.words_shown):
            return True
        else:
            return False

    def answer(self, answer: str) -> None:
        """
        What to do when answer is inputted.
        """
        if self.is_correct(answer):
            self.points += 1
            self.words_shown.append(self.curr_word)
            self.curr_word_randomizer()
        else:
            self.setup()

    def curr_word_randomizer(self) -> None:
        """
        Make self.curr_word either new word or an already seen word.
        """
        temp = random.choice(self.words_shown)
        if random.randint(1, 2) == 2 and len(self.words_shown) > 0 and \
                temp != self.curr_word:
            self.curr_word = temp
        else:
            self.curr_word = self.game_words[self.points]
