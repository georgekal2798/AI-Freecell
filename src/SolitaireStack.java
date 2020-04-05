import java.util.Stack;

public abstract class SolitaireStack {
    private Stack<Card> cards;

    public SolitaireStack(Stack<Card> cards) {
        this.cards = cards;
    }

    public Stack<Card> getCards() {
        return cards;
    }

    public boolean isEmpty(){
        return this.getCards().empty();
    }

    public abstract boolean canMove(SolitaireStack sourceStack);

    public void move(SolitaireStack sourceStack){
        Card newCard = sourceStack.top();
        Card topCard = this.isEmpty() ? null : this.top();

        this.add(sourceStack.getCards().pop());
        Global.logMove(this.moveMessage(topCard, newCard));
    }

    protected abstract String moveMessage(Card topCard, Card newCard);

    public void add(Card c){
        this.getCards().push(c);
    }

    public Card top(){
        return this.getCards().peek();
    }
}
