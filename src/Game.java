public abstract class Game {

    private static LowerStack[] stacks = new LowerStack[8];
    private static Foundation[] foundations = new Foundation[4];
    private static Freecell[] freecells = new Freecell[4];

    public static LowerStack[] getStacks() {
        return stacks;
    }

    public static Foundation[] getFoundations() {
        return foundations;
    }

    public static Freecell[] getFreecells() {
        return freecells;
    }

    public static void printStacks(){
        for (LowerStack s : stacks){
            System.out.print("\n");
            for (Card c : s.getCards()){
                System.out.print(c.getCardName() + " ");
            }
        }
    }
}
