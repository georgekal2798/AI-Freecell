import java.util.Stack;

public class Freecell extends SolitaireStack {

    public Freecell(Stack<Card> cards) {
        super(cards);
    }

    @Override
    public boolean canMove(SolitaireStack sourceStack) {
        if (sourceStack.isEmpty()) return false;
        return this.isEmpty();
    }

    @Override
    protected String moveMessage(Card topCard, Card newCard) {
        return "freecell " + newCard.getCardName();
    }
}
