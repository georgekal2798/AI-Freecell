from solitaire_stack import SolitaireStack


class Foundation(SolitaireStack):
    def __init__(self):
        super().__init__()

    def can_move(self, source_stack):
        if source_stack.is_empty():
            return False
        elif self.is_empty():
            if source_stack.top().number == 0:
                # This foundation is empty and the new card is an ace (in that case a 0)
                return True
            else:
                return False
        else:
            # The card from the source stack is greater by one than the on this stack
            greater_by_one = source_stack.top().number - self.top().number == 1
            # The two cards are of the same suit
            same_suit = source_stack.top().suit == self.top().suit

            if same_suit and greater_by_one:
                return True
            else:
                return False

    def move_message(self, top, new):
        return 'foundation ' + new.name()
