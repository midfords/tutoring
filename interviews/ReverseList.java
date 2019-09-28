import java.util.*;

public class ReverseList {
    
    public static void main(String[] args) {

        Node n0 = new Node();
        n0.value = 1;
        n0.next = new Node();
        n0.next.value = 2;
        n0.next.next = new Node();
        n0.next.next.value = 3;

        print(n0);

        Node r = reverse(n0);

        print(r);
    }

    private static void print(Node n) {
        Node curr = n;

        while(curr != null) {
            System.out.print(curr.value + " -> ");
            curr = curr.next;
        }

        System.out.println();
    }

    private static Node reverse(Node n) {
        if (n == null)
            return null;

        Node prev = null; 
        Node current = n; 
        Node next = null; 
        while (current != null) { 
            next = current.next; 
            current.next = prev; 
            prev = current; 
            current = next; 
        } 
        n = prev; 
        return n; 
    }

    private static class Node {
        Node next;
        int value;
    }
}