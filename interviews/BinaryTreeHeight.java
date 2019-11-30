/**
 * Binary Tree Height
 * 
 * Write a method that returns the height of a binary tree recursively. 
 * Height is the number of hops between the root node and the lowest point
 * of the binary tree. The binary tree is not balanced.
 * 
 * Example
 *      o
 *     / \
 *    o   o      -> 3
 *   /
 *  o
 * Explanation: The longest path to a null node is 3, thus the height is 3.
 */

public class BinaryTreeHeight {
  int binaryTreeHeight(TreeNode n) {

    int largerHeight;
    int leftHeight = 0;
    int rightHeight = 0;

    if (n == null)  {
      return 0;
    }

    leftHeight = height(n.left());
    rightHeight = height(n.right());

    if(leftHeight > rightHeight) {
      largerHeight = leftHeight;
    } else {
      largerHeight = rightHeight;
    }

    return largerHeight + 1;  
  }
}
