/**
 * Cycle Finder
 * 
 * Given a linked list, determine if there is a cycle present.
 * 
 * Example: (1)->(2)->(3)->null -> false
 * Example: (1)->(2) -> true
 *           ^----'
 */

import java.util.*;

public class CycleFinder {
    
    public static void main(String[] args) {

        Node n0 = new Node();
        n0.next = n0;

        Node n1 = null;

        Node n2 = new Node();
        n2.next = new Node();
        n2.next.next = new Node();

        boolean b0 = detectCycle(n0);
        boolean b1 = detectCycle(n1);
        boolean b2 = detectCycle(n2);

        System.out.println("Result: " + b0);
        System.out.println("Result: " + b1);
        System.out.println("Result: " + b2);

    }

    private static boolean detectCycle(Node n) {
        if (n == null)
            return false;

        Set<Node> k = new HashSet<>();

        Node curr = n;
        while(curr != null) {
            if (k.contains(curr))
                return true;

            k.add(curr);
            curr = curr.next;
        }

        return false;
    }

    private static class Node {
        Node next;
        int value;
    }
}