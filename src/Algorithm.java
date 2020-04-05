import java.util.Stack;

public abstract class Algorithm {
    private int numberOfMoves;

    public Algorithm() {

    }

    public abstract void run();

    public void stop(){
        FileManager.closeFiles(numberOfMoves);
    }

    public void countMove(){
        numberOfMoves++;
    }
}
