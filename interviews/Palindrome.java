
public class Palindrome {
    public static void main(String[] args) {

        String s0 = null;
        String s1 = "";
        String s2 = "abc";
        String s3 = "abcba";

        boolean b0 = palindrome(s0);
        boolean b1 = palindrome(s1);
        boolean b2 = palindrome(s2);
        boolean b3 = palindrome(s3);

        System.out.println(b0);
        System.out.println(b1);
        System.out.println(b2);
        System.out.println(b3);
    }

    private static boolean palindrome(String s) {
        if (s == null) 
            return false;

        int l = s.length();
        for (int i = 0; i < l / 2; i++) {
            if (s.charAt(i) != s.charAt(l-i-1))
                return false;
        }

        return true;
    }
}