/**
 * Console Print
 * 
 * Given a sentance as a string (or array of words as strings), console width
 * and console height, determin how many times the sentance can be printed on
 * the simulated console. Words must not be truncated by the end of the line.
 * Words must also be separated by spaces, but only when that word is not the
 * last on line.
 * For example, the phrase hello world, and a 7 x 2 console would produce:
 *    |h|e|l|l|o| | |
 *    |w|o|r|l|d| | |
 * Therefor the sentance can be printed once.
 * 
 * Example: 'hello world', 3, 7 -> 1
 *    |h|e|l|l|o| | |
 *    |w|o|r|l|d| | |
 *    |h|e|l|l|o| | |
 * Example: 'my dog dude', 5, 6 -> 2
 *    |m|y| |d|o|g|
 *    |d|u|d|e| | |
 *    |m|y| |d|o|g|
 *    |d|u|d|e| | |
 *    |m|y| |d|o|g|
 * Example: 'looooooong', 1, 1000 -> 0
 */

public class ConsolePrint {
    public static void main(String[] args) {

        String[] phrase = {"This", "is", "a", "really", "long", "phrase", "something"};

        int t0 = simulatePrint(phrase, 1, 20);
        int t1 = simulatePrint(phrase, 2, 20);
        int t2 = simulatePrint(phrase, 10, 20);

        System.out.println(t0);
        System.out.println(t1);
        System.out.println(t2);
    }

    private static int simulatePrint(String[] phrase, int w, int h) {

        int index = 0;
        int count = 0;
        int i = 0;
        int j = 0;

        while(i < w) {
            while(j < h) {
                if (phrase[index].length() <= w - i) {
                    i += phrase[index].length() + 1;
                    index ++;
                } else {
                    i = 0;
                    j ++;
                }

                if (index >= phrase.length) {
                    count ++;
                    index = 0;
                }
            }
            i++;
        }

        return count;
    }

}