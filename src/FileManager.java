import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public abstract class FileManager {
    public final int N = 13;

    public static Scanner scanner;
    public static String outputPath;
    public static String movesLogger = "";

    public static void logMove(String moveMessage) {
        movesLogger += "\n" + moveMessage;
    }

    public static void closeFiles(int numberOfMoves) {
        movesLogger = movesLogger.replace("%NUM_OF_MOVES%", String.valueOf(numberOfMoves));

        try {
            FileWriter outputFile = new FileWriter(outputPath);
            outputFile.write(movesLogger);
            outputFile.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void openFiles(String inputPath, String outputPath) {
        File inputFile = new File(inputPath);
        try {
            scanner = new Scanner(inputFile);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        parseData();
        scanner.close();

        movesLogger += "%NUM_OF_MOVES%";
    }

    private static void parseData() {
        char suitChar;
        Suit suit;
        for (int i = 0; scanner.hasNextLine(); i++){
            while (scanner.hasNext()){
                suitChar = scanner.next().charAt(0);

                switch (suitChar){
                    case 'S':
                        suit = Suit.SPADES;
                        break;
                    case 'C':
                        suit = Suit.CLUBS;
                        break;
                    case 'H':
                        suit = Suit.HEARTS;
                        break;
                    case 'D':
                        suit = Suit.DIAMONDS;
                        break;
                    default:
                        throw new IllegalStateException("Unexpected value: " + suitChar);
                }

                Game.getStacks()[i].getCards().push(new Card(scanner.nextInt(), suit));
            }
        }
    }
}
