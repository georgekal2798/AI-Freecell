import file_manager


class SolitaireStack:
    def __init__(self):
        self.cards = []

    def is_empty(self):
        return not self.cards

    def can_move(self, source_stack):
        pass

    def move(self, source_stack):
        new = source_stack.cards.pop()
        top = self.top()

        self.add(new)
        file_manager.log_move(self.move_message(top, new))

    def add(self, card):
        self.cards.append(card)

    def top(self):
        if self.cards:
            return self.cards[-1]
        return None

    def move_message(self, top, new):
        pass
