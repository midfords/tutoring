/**
 * Brackets
 * 
 * Given a string (or char array) of characters, determin if the parenthesis are valid.
 * 
 * Example: '(hello world)' -> true
 * Example: '(hello (world))' -> true
 * Explanation: Every opening parenthesis has a valid closing parenthesis.
 * 
 * Example: '(ab(cd' -> false
 * Explanation: Every opening parenthesis does not have a corresponding closing parenthesis.
 */

import java.util.*;

public class Brackets {
    public static void main(String[] args) {

        char[] c0 = new char[]{'(', '(', '.', ')', '.', '.'};
        char[] c1 = new char[]{'(', '(', '(', '(', ')', ')'};
        char[] c2 = new char[]{'(', '(', '.', '.', ')', ')'};
        char[] c3 = new char[]{'(', ')', '(', '(', ')', ')'};

        System.out.println(isBalanced(c0));
        System.out.println(isBalanced(c1));
        System.out.println(isBalanced(c2));
        System.out.println(isBalanced(c3));
    }

    private static boolean isBalanced(char[] c) {
        if (c == null)
            return false;
        if (c.length == 0)
            return true;

        Stack<Character> k = new Stack<>();

        for (int i = 0; i < c.length; i++) {
            if (c[i] == '(')
                k.push('(');
            if (c[i] == ')')
                k.pop();
        }

        return k.isEmpty();
    }
}