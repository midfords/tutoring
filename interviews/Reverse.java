/**
 * Reverse
 * 
 * Given a string, return the reversed string.
 * 
 * Example: 'abc' -> 'cba'
 */

public class Reverse {

    public static void main (String[] args) {

        String s0 = null;
        String s1 = "";
        String s2 = "Hello World!";

        String s0a = reverse(s0);
        String s1a = reverse(s1);
        String s2a = reverse(s2);

        System.out.println(s0 + " -> " + s0a);
        System.out.println(s1 + " -> " + s1a);
        System.out.println(s2 + " -> " + s2a);
    }

    private static String reverse(String s) {
        if (s == null)
            return null;

        byte[] bytes = s.getBytes();
        int l = bytes.length;
        for (int i = 0; i < l / 2; i++) {
            byte t = bytes[i];
            bytes[i] = bytes[l-i-1];
            bytes[l-i-1] = t;
        }

        return new String(bytes);
    }
}
