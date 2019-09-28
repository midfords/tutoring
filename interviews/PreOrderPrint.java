
public class PreOrderPrint {
    public static void main(String[] args) {
        Node t = getTree();

        preOrderPrint(t);

        System.out.println("Max: " + max(t));
    }

    private static void preOrderPrint(Node r) {
        if (r == null)
            return;

        preOrderPrint(r.left);

        System.out.println(r.value);

        preOrderPrint(r.right);
    }

    private static int bigger(int a, int b) {
        if (a > b)
            return a;
        else 
            return b;
    }

    private static int max(Node n) {
        if (n.left == null && n.right == null)
            return n.value;

        if (n.left != null && n.right != null)
            return bigger(max (n.left), max(n.right));

        if (n.left != null)
            return max(n.left);

        return max(n.right);
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

    private static class Node {
        Node left;
        Node right;
        int value;
    }
}
