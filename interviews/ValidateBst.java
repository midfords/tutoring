import java.util.*;

public class ValidateBst {

    public static void main(String[] args) {

        Node n0 = getTree();
        Node n1 = getBstTree();

        System.out.println(isBst(n0));
        System.out.println(isBst(n1));
    }

    private static boolean isBst(Node n) {
        return isBstAux(n);
    }

    private static void preOrderPrint(Node r, List<Integer> l) {
        if (r == null)
            return;

        preOrderPrint(r.left, l);

        l.add(r.value);

        preOrderPrint(r.right, l);
    }

    private static boolean isBstAux(Node n) {
        List<Integer> l = new ArrayList<>();

        preOrderPrint(n, l);
        boolean f = true;
        for (int i = 1; i < l.size(); i++) {
            f = f && l.get(i-1) < l.get(i);
        }

        return f;
    }

    private static Node getTree() {
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

        n0.left = n1;
        n0.right = n2;
        n1.left = n3;
        n3.right = n4;
        n2.left = n5;
        n2.right = n6;

        return n0;
    }

    private static Node getBstTree() {
        Node n0 = new Node();
        n0.value = 5;
        Node n1 = new Node();
        n1.value = 3;
        Node n2 = new Node();
        n2.value = 7;
        Node n3 = new Node();
        n3.value = 1;
        Node n4 = new Node();
        n4.value = 2;
        Node n5 = new Node();
        n5.value = 6;
        Node n6 = new Node();
        n6.value = 8;

        n0.left = n1;
        n0.right = n2;
        n1.left = n3;
        n3.right = n4;
        n2.left = n5;
        n2.right = n6;

        return n0;
    }

    private static class Node {
        Node left;
        Node right;
        int value;
    }
}