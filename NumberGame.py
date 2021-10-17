import random


class NumberGame:
    """
    A class representing the internal workings of the number memory game.
    """
    points: int = 0
    curr_num: str
    lower_bound: int = 1
    time_on_screen: float = 1.7
    begin: bool = False

    def __init__(self):
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
