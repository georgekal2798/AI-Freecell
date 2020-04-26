from collections import deque

import file_manager


class SolitaireStack:
    def __init__(self):
        self.cards = deque()

    def __eq__(self, other):
        return self.cards == other.cards

    def __ne__(self, other):
        return self.cards != other.cards

    def __hash__(self):
        return hash(tuple(self.cards))

    def is_empty(self):
        return not self.cards

    def can_move(self, source_stack):
        pass

    def move(self, source_stack):
        new = source_stack.cards.pop()
        top = self.top()

        self.add(new)

        return self.move_message(top, new)

    def add(self, card):
        self.cards.append(card)

    def top(self):
        if self.cards:
            return self.cards[-1]
        return None

    def move_message(self, top, new):
        pass
