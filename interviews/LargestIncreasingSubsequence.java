
public class LargestIncreasingSubsequence {
    public static void main(String[] args) {

        int[] a0 = new int[]{1};
        int[] a1 = new int[]{1, 2, 3};
        int[] a2 = new int[]{1, 2, 1, 3};
        int[] a3 = new int[]{1, 2, 1, 2, 3, 1, 3, 4, 5, 1, 2, 3, 6};
        int[] a4 = new int[]{10, 9, 2, 5, 3, 7, 101, 18};

        int l0 = largestIncreasingSubsequence(a0);
        int l1 = largestIncreasingSubsequence(a1);
        int l2 = largestIncreasingSubsequence(a2);
        int l3 = largestIncreasingSubsequence(a3);
        int l4 = largestIncreasingSubsequence(a4);

        System.out.println(l0);
        System.out.println(l1);
        System.out.println(l2);
        System.out.println(l3);
        System.out.println(l4);
    }

    private static int largestIncreasingSubsequence(int[] a) {
        if (a == null || a.length == 0)
            return 0;

        int[] f = new int[a.length];
        f[0] = 1;

        for(int i = 1; i < a.length; i++) {

            int max = 1;
            for(int j = 0; j < i; j++) {

                if (a[j] < a[i] && f[j] >= max) {
                    max = f[j] + 1;
                }
            }

            f[i] = max;
        }

        int max = f[0];
        for (int i = 1; i < f.length; i++) {
            if (f[i] > max)
                max = f[i];
        }

        return max;
    }
}