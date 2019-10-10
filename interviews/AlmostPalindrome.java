
public class AlmostPalindrome {
    public static void main (String [] args) {
        System.out.println("Is Palindrome:");
        System.out.println(" : " + isPalindrome("", 0, 0));
        System.out.println("a : " + isPalindrome("a", 0, 1));
        System.out.println("ab : " + isPalindrome("ab", 0, 1));
        System.out.println("abba : " + isPalindrome("abba", 0, 3));
        System.out.println("abba : " + isPalindrome("abba", 0, 2));

        System.out.println("Is Almost Palindrome");
        System.out.println(" : " + isAlmostPalindrome(""));
        System.out.println("a : " + isAlmostPalindrome("a"));
        System.out.println("ab : " + isAlmostPalindrome("ab"));
        System.out.println("abbca : " + isAlmostPalindrome("abbca"));
        System.out.println("abbcda : " + isAlmostPalindrome("abbcda"));
    }

    // private static boolean isAlmostPalindrome(String s) {
    //     if (isPalindrome(s))
    //         return false;

    //     for (int i = 0; i < s.length(); i++) {
    //         String t = s.substring(0, i) + s.substring(i + 1);
    //         if (isPalindrome(t))
    //             return true;
    //     }
    //     return false;
    // }

    private static boolean isPalindrome(String s, int start, int end) {
        for (int i = start; i < start + ((end - start) / 2); i++) {
            if (s.charAt(i) != s.charAt(end - i + start))
                return false;
        }
        return true;
    }

    private static boolean isAlmostPalindrome(String s) {
        if (s == null || s.length() == 0)
            return false;

        int i = 0;
        int j = s.length() - 1;

        while(i < j) {
            if (s.charAt(i) != s.charAt(j))
                return isPalindrome(s, i + 1, j) || isPalindrome(s, i, j - 1);
            i++;
            j--;
        }

        return false;
    }
}