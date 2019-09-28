import java.util.*;

public class RemoveDups {
    
    public static void main(String[] args) {

        Node n0 = new Node();
        n0.value = 1;
        n0.next = new Node();
        n0.next.value = 2;
        n0.next.next = new Node();
        n0.next.next.value = 3;
        n0.next.next.next = new Node();
        n0.next.next.next.value = 2;

        print(getList());

        Node r = removeDups(getList());

        print(r);
    }

    private static Node getList() {
        Node n0 = new Node();
        n0.value = 2;
        Node n1 = new Node();
        n1.value = 1;
        Node n2 = new Node();
        n2.value = 4;
        Node n3 = new Node();
        n3.value = 1;
        Node n4 = new Node();
        n4.value = 1;
        Node n5 = new Node();
        n5.value = 1;
        Node n6 = new Node();
        n6.value = 6;
        Node n7 = new Node();
        n7.value = 1;

        n0.next = n1;
        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n5;
        n5.next = n6;
        n6.next = n7;

        return n0;
    }

    private static void print(Node n) {
        Node curr = n;

        while(curr != null) {
            System.out.print(curr.value + " -> ");
            curr = curr.next;
        }

        System.out.println();
    }

    private static Node removeNext(Node n) {
        if (n == null || n.next == null) 
            return n;

        n.next = n.next.next;

        return n;
    }

    private static Node removeDups(Node head) {
        if (head == null)
            return null;

        Set<Integer> k = new HashSet<>();

        Node curr = head;
        Node next = head.next;
        while(curr != null && next != null) {
            k.add(curr.value);

            if (k.contains(next.value)) {
                removeNext(curr);
            } else {
                curr = curr.next;
            }
            next = curr.next;

            System.out.println(k.toString());
        }

        return head;
    }

    private static class Node {
        Node next;
        int value;
    }
}