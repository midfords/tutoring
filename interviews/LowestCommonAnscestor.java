/**
 * Lowest Common Anscestor
 * 
 * Given a binary, find the lowest common anscestor for two nodes.
 *       4
 *    2     6
 *   1 3   5 7
 *
 * Example: 1,3 -> 2
 * Explanation: The lowest common node for '1' and '3' is the parent node '2'.
 * 
 * Example: 1,5 -> 4
 * Explanation: The lowest common node for '1' and '5' is the root node '4'.
 */

public class LowestCommonAnscestor {
    public static void main(String[] args) {
        Node n0 = getTree1();
        Node n1 = getTree2();

        System.out.println(findLca(n0, 1, 2));
        System.out.println(findLca(n0, 6, 11));
        System.out.println(findLca(n0, 3, 4));

        System.out.println(findLca(n1, 1, 2));
        System.out.println(findLca(n1, 7, 1));
        System.out.println(findLca(n1, 8, 2));
    }

    private static int findLca(Node n, int v0, int v1) {
        if (n == null)
            return -1;

        int result = -1;

        if (findLcaAux(n, v0, v1) >= 2)
            result = n.value;

        findLca(n.left, v0, v1);
        findLca(n.right, v0, v1);

        return result;
    }

    private static int findLcaAux(Node n, int v0, int v1) {
        if (n == null)
            return 0;

        int c = 0;

        c += findLcaAux(n.left, v0, v1);
        c += findLcaAux(n.right, v0, v1);

        if (n.value == v0 || n.value == v1)
            c++;

        return c;
    }

    private static Node getTree1() {
        Node n0 = new Node();
        n0.value = 2;
        Node n1 = new Node();
        n1.value = 1;
        Node n2 = new Node();
        n2.value = 4;
        Node n3 = new Node();
        n3.value = 3;
        Node n4 = new Node();
        n4.value = 7;
        Node n5 = new Node();
        n5.value = 10;
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

    private static Node getTree2() {
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