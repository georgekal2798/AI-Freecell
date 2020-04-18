from solitaire_stack import SolitaireStack


class BaseStack(SolitaireStack):
    def __init__(self):
        super().__init__()

    def can_move(self, source_stack):
        if source_stack.is_empty():
            return False
        elif self.is_empty():
            return True
        else:
            # The card from the source stack has a different color than the one on this stack
            different_colors = source_stack.top().color() != self.top().color()
            # The card from the source stack is lesser by one than the on this stack
            lesser_by_one = source_stack.top().number - self.top().number == -1.

            if different_colors and lesser_by_one:
                return True
            else:
                return False

    def move_message(self, top, new):
        if not top:  # If there's not a card on this stack, new card is moved to a new stack
            return 'newstack ' + new.name()
        else:
            return 'stack ' + new.name() + ' ' + top.name()
