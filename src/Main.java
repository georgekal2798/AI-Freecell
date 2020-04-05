public class Main {

    private static Algorithm algorithm;
    private static String inputPath;
    private static String outputPath;

    public static void main(String[] args) {
        defineAlgorithm(args[0]);
        setFilePaths(args[1], args[2]);

        init();

        algorithm.run();
    }

    private static void init(){
        FileManager.openFiles(inputPath, outputPath);
    }

    private static void defineAlgorithm(String arg){
        switch (arg){
            case "breadth":
                algorithm = new Breadth();
                break;
            case "depth":
                algorithm = new Depth();
                break;
            case "best":
                algorithm = new Best();
                break;
            case "astar":
                algorithm = new AStar();
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + arg);
        }
    }

    public static void setFilePaths(String inputPath, String outputPath) {
        Main.inputPath = inputPath;
        Main.outputPath = outputPath;
    }
}
