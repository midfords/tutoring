

public class CloneLinkedList {

    public static void main(String[] args) {
        Node l = getList();

        print(l);

        Node c = clone(l);

        print(c);
    }

    private static void print(Node n) {
        Node curr = n;

        while(curr != null) {
            System.out.print(curr.value + " -> ");
            curr = curr.next;
        }

        System.out.println();

        curr = n;

        while(curr != null) {
            if (curr.arbt != null)
                System.out.print(curr.arbt.value + "    ");
            else
                System.out.print(".    ");
            curr = curr.next;
        }

        System.out.println();

    }

    private static Node clone(Node node) {
        Node head = cloneAux(node);

        Node curr = head;
        Node orig = node;
        while(curr != null) {
            curr.arbt = curr.arbt.arbt.next;
            curr = curr.next;
            orig = orig.next;
        }

        return head;
    }

    private static Node cloneAux(Node node) {
        if (node == null)
            return null;

        Node head = new Node();
        head.value = node.value;

        Node tail = cloneAux(node.next);
        node.next = head;
        head.arbt = node;
        head.next = tail;

        return head;
    }

    private static Node getList() {
        Node n0 = new Node();
        n0.value = 1;
        Node n1 = new Node();
        n1.value = 2;
        Node n2 = new Node();
        n2.value = 3;
        Node n3 = new Node();
        n3.value = 4;
        Node n4 = new Node();
        n4.value = 5;
        Node n5 = new Node();
        n5.value = 6;
        Node n6 = new Node();
        n6.value = 7;

        n0.next = n1;
        n0.arbt = n4;

        n1.next = n2;
        n1.arbt = n3;

        n2.next = n3;
        n2.arbt = n6;

        n3.next = n4;
        n3.arbt = n5;

        n4.next = n5;
        n4.arbt = n1;

        n5.next = n6;
        n5.arbt = n2;

        n6.arbt = n0;

        return n0;
    }

    private static class Node {
        Node next;
        Node arbt;
        int value;
    }
}