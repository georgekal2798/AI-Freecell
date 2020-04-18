from solitaire_stack import SolitaireStack


class Freecell(SolitaireStack):
    def __init__(self):
        super().__init__()

    def can_move(self, source_stack):
        if type(source_stack) is Freecell:
            # There is no point in moving a card from one freecell to another
            return False
        # As long as this freecell is empty and the source stack has cards, move the card
        return self.is_empty() and not source_stack.is_empty()

    def move_message(self, top, new):
        return 'freecell ' + new.name()
