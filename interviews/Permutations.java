/**
 * Permutations
 * 
 * Given a string, print all permutations of the string including the empty string.
 * The number of permutations should be the length of the string 2 ^ L
 * 
 * Example: 'abc' -> '', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'
 */

import java.lang.*;

public class Permutations {
    public static void main(String[] args) {

        String s0 = null;
        String s1 = "";
        String s2 = "abcdef";

        printPermutations(s0);

        printPermutations(s1);

        printPermutations(s2);
    }

    private static void printPermutations(String s) {
        if (s == null) return;

        int mask = 0;
        int max = ((int) Math.pow(2, s.length())) - 1;

        while (mask <= max) {
            printPermutation(s, mask);
            mask ++;
        }
    }

    private static void printPermutation(String s, int mask) {
        String p = "";

        int i = 1;
        int index = 0;
        int max = ((int) Math.pow(2, s.length())) - 1;

        while (i < max) {
            if ((i & mask) > 0) {
                p += s.charAt(index);
            }

            i = i << 1;
            index ++;
        }

        System.out.println(p);
    }
}
