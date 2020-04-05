import java.util.Stack;

public class LowerStack extends SolitaireStack{

    public LowerStack(Stack<Card> cards) {
        super(cards);
    }

    @Override
    public boolean canMove(SolitaireStack sourceStack){
        if (sourceStack.isEmpty()) return false;
        return (sourceStack.top().getColor() != this.top().getColor()
                && sourceStack.top().getNumber() - this.top().getNumber() == -1)
                || this.isEmpty();
    }

    @Override
    protected String moveMessage(Card topCard, Card newCard) {
        if (topCard == null){
            return "newstack " + newCard.getCardName();
        }
        else return "stack " + newCard.getCardName() + " " + topCard.getCardName();
    }
}
