import java.util.Stack;

public class Foundation extends SolitaireStack{

    public Foundation(Stack<Card> cards) {
        super(cards);
    }

    @Override
    public boolean canMove(SolitaireStack sourceStack) {
        if (sourceStack.isEmpty()) return false;
        return (sourceStack.top().getNumber() - this.top().getNumber() == 1
                && sourceStack.top().getSuit() == this.top().getSuit())
                || (this.isEmpty() && sourceStack.top().getNumber() == 0);
    }

    @Override
    protected String moveMessage(Card topCard, Card newCard) {
        return "foundation " + newCard.getCardName();
    }
}
