from model.foundation import Foundation
from model.solitaire_stack import SolitaireStack


class Freecell(SolitaireStack):
    def __init__(self):
        super().__init__()

    def can_move(self, source_stack):
        if type(source_stack) is Freecell or type(source_stack) is Foundation:
            # There is no point in moving a card from one freecell to another or from a foundation to a freecell
            return False
        # As long as this freecell is empty and the source stack has cards, move the card
        return self.is_empty() and not source_stack.is_empty()

    def move_message(self, top, new):
        return 'freecell ' + new.name()
