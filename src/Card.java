public class Card {

    private int number;
    private Suit suit;

    public Card(int number, Suit suit) {
        this.number = number;
        this.suit = suit;
    }

    public int getNumber() {
        return number;
    }

    public Suit getSuit() {
        return suit;
    }

    public Color getColor() {
        switch (this.getSuit()) {
            case HEARTS:
            case DIAMONDS:
                return Color.RED;
            case SPADES:
            case CLUBS:
                return Color.BLACK;
            default:
                throw new IllegalStateException("Unexpected value: " + this.getSuit());
        }
    }

    public String getCardName(){
        String prefix;
        switch (this.getSuit()){
            case SPADES:
                prefix = "S";
                break;
            case HEARTS:
                prefix = "H";
                break;
            case DIAMONDS:
                prefix = "D";
                break;
            case CLUBS:
                prefix = "C";
                break;
            default:
                prefix = "";
        }

        return prefix + this.getNumber();
    }

}
