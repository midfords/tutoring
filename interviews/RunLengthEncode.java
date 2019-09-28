
public class RunLengthEncode {

    public static void main(String[] args) {

        String s0 = null;
        String s1 = "";
        String s2 = "abc";
        String s3 = "aaaabbbcccccc";

        System.out.println(s0 + " -> " + encode(s0));
        System.out.println(s1 + " -> " + encode(s1));
        System.out.println(s2 + " -> " + encode(s2));
        System.out.println(s3 + " -> " + encode(s3));
    }

    private static String encode(String s) {
        if (s == null)
            return null;
        if (s == "")
            return "";

        String e = "";
        int count = 1;
        char c = s.charAt(0);

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                count ++;
            } else {
                e += c;
                e += count;
                count = 1;
            }
            c = s.charAt(i);
        }

        e += c;
        e += count;

        return e;
    }
}