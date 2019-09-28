import java.util.*;

public class ThirdLast {
    
    public static void main(String[] args) {

        Node list = getList();

        print(list);

        int v = findThirdLast(list);

        System.out.println("Third last: " + v);
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

        n0.next = n1;
        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n5;
        n5.next = n6;

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

    private static int findThirdLast(Node head) {
        if (head == null || head.next == null || head.next.next == null)
            return -1;

        Node curr0 = head;
        Node curr3 = head.next.next.next;
        while(curr3 != null) {

            curr0 = curr0.next;
            curr3 = curr3.next;
        }

        return curr0.value;
    }

    private static class Node {
        Node next;
        int value;
    }
}