/**
 * Delete List
 * 
 * Delete all nodes in a linked list, so that there are no memory leaks. 
 * Write two versions, one recursive and one iterative.
 */

public class DeleteLinkedList {
  void deleteLinkedList(Node head) {
    Node deleteNode = head;

    while(head != null) {
      Node cur = head;
      while(cur.next != null) {
        deleteNode = cur.next;
      }
      delete(deleteNode);
    }
  }

  void deleteLinkedList(Node head) {
    if (head == null) {
      return;
    }

    deleteLinkedList(head.next;
    delete(head);
  }

  void delete(Node node) {
    System.out.println(node.value + " deleted.");
  }

  private class Node {
    Node next;
    int value;
  }
}
