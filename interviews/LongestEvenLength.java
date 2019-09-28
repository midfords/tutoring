

public class LongestEvenLength {

    public static void main(String[] args) {
        String s0 = "";
        String s1 = "123123";
        String s2 = "1538023";
        String s3 = "1231231538023";

        System.out.println(s0 + " -> " + longestEvenLength(s0));
        System.out.println(s1 + " -> " + longestEvenLength(s1));
        System.out.println(s2 + " -> " + longestEvenLength(s2));
        System.out.println(s3 + " -> " + longestEvenLength(s3));
    }

    private static int toInt(char c) {
        return c - '0';
    }

    private static int longestEvenLength(String s) {
        if (s == null || s.length() <= 1)
            return 0;

        int max = 0;
        for (int j = 0; j < s.length(); j++) {
            int lsum = 0;
            int rsum = 0;
            int lindex = j;
            int rindex = j + 1;

            while(lindex >= 0 && rindex < s.length()) {
                lsum += toInt(s.charAt(lindex));
                rsum += toInt(s.charAt(rindex));

                if (lsum == rsum && rindex - lindex + 1 > max) {
                    max = rindex - lindex + 1;
                }

                lindex --;
                rindex ++;
            }
        }

        return max;
    }

}
