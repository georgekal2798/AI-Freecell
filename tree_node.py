import data
from model.card import Card
from model.freecell import Freecell


class TreeNode:
    def __init__(self, parent, base_stacks, foundations, freecells, depth, moves_logger='%NUM_OF_MOVES%'):
        self.parent = parent
        self.base_stacks = base_stacks
        self.foundations = foundations
        self.freecells = freecells
        self.depth = depth
        self.heuristic_value = 0
        self.number_of_moves = 0
        self.moves_logger = moves_logger

    def __eq__(self, other):
        return (self.base_stacks == other.base_stacks) and \
               (self.foundations == other.foundations) and \
               (self.freecells == other.freecells)

    def __hash__(self):
        return hash(tuple(self.base_stacks + self.foundations + self.freecells))

    def find_possible_moves(self):
        # possible_moves is a set of tuples. The first value of each tuple is the index of the source stack and the
        # second value is the index of the target stack. Indices reference to the list returned by self.all_stacks()
        possible_moves = set()

        # self.all_stacks() returns a list of SolitaireStack objects that contains:
        # positions 0 - S-1: Base stacks
        # positions S - S+F-1: Foundations
        # positions S+F - S+F+C-1: Freecells
        #
        # Values of S, F, C are defined in data.py

        freecells_range = range(data.S + data.F, data.S + data.F + data.C)

        for i, current_stack in enumerate(self.base_stacks + self.freecells):
            i_to_freecell = False
            if type(current_stack) is Freecell:
                i += data.F
            for j, other_stack in enumerate(self.all_stacks()):
                if current_stack != other_stack and other_stack.can_move(current_stack):
                    if i_to_freecell and j in freecells_range:
                        continue
                    possible_moves.add((i, j))
                    if j in freecells_range:
                        i_to_freecell = True

        # Variable i_to_freecell is used to filter possible_moves: if a card from stack i is already set to move to a
        # freecell, a move from i to another freecell will not be added to possible_moves again

        return possible_moves

    def all_stacks(self):
        return self.base_stacks + self.foundations + self.freecells

    def log_move(self, message):
        # self.number_of_moves += 1
        self.moves_logger += '\n' + message

    def calculate_heuristic(self, include_moves=0):
        # Based on this paper:
        # http://www.genetic-programming.org/hc2011/06-Elyasaf-Hauptmann-Sipper/Elyasaf-Hauptmann-Sipper-Paper.pdf
        #
        # For each foundation stack, locate within the base stacks the next card that should be placed there, and count
        # the cards found on top of it. The returned value is the sum of this count for all foundations. This number is
        # multiplied by 2 if there are no free freecells or empty foundation stacks (reflecting the fact that freeing
        # the next card is harder in this case).

        cards_left = 4 * data.N
        value = 0
        for f in self.foundations:
            # Counts how many cards are left to be put to the foundations
            cards_left -= len(f.cards)
            if not f.is_empty():
                if f.top().number == data.N:
                    # This foundation is full. No cards left to be added
                    continue
                else:
                    card = Card(f.top().number + 1, f.suit)
            else:
                card = Card(Card.ACE, f.suit)

            for i, s in enumerate(self.base_stacks):
                if card in s.cards:
                    value += i
                    # value += 2*i
                    break

        # If freecells are not full, value is divided by 2
        # for c in self.freecells:
        #     if c.is_empty():
        #         value /= 2
        #         break

        value += cards_left

        # include_moves is different than zero only when A* search algorithm is used. In that case the number of moves
        # already made is added to the final heuristic value
        self.heuristic_value = value + include_moves
