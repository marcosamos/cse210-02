import random


class Card:

    def __init__(self):


        self.value = 0
        self.points = 0

    def draw_card(self):

        self.value = random.randint(1,13)
        # I need to check this if statement and validate with the instance of director. (do_udates)
        self.points = 100 if self.value == "h" else 75 if self.value == "l" else 0
