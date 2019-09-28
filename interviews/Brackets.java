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