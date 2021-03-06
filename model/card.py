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

    # Override that allows comparisons between Card objects
    def __eq__(self, other):
        return self.suit == other.suit and self.number == other.number

    # Override that allows TreeNode objects to be part of a set
    def __hash__(self):
        return hash((self.suit, self.number))

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
