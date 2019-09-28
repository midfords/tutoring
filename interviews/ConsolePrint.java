
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