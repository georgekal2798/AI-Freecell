from enum import Enum


class Suit(Enum):
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3
    HEARTS = 4


class Color(Enum):
    RED = 1
    BLACK = 2


class Card:
    ACE = 1

    def __init__(self, number, suit):
        self.suit = suit
        self.number = number

    def name(self):
        switch = {
            Suit.HEARTS: 'H',
            Suit.DIAMONDS: 'D',
            Suit.CLUBS: 'C',
            Suit.SPADES: 'S'
        }
        return switch.get(self.suit, None) + str(self.number)

    def color(self):
        if self.suit in (Suit.HEARTS, Suit.DIAMONDS):
            return Color.RED
        elif self.suit in (Suit.CLUBS, Suit.SPADES):
            return Color.BLACK
        else:
            return None
