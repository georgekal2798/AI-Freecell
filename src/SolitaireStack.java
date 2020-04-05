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
        Card newCard = sourceStack.getCards().pop();
        Card topCard = this.top();

        this.add(newCard);
        FileManager.logMove(this.moveMessage(topCard, newCard));
    }

    protected abstract String moveMessage(Card topCard, Card newCard);

    public void add(Card c){
        this.getCards().push(c);
    }

    public Card top(){
        if (this.isEmpty()) return null;
        return this.getCards().peek();
    }
}
