/* Given the head of a linked list, remove the nth node from the end of the list and return its head. */

class ListNode {
    int val;
    ListNode next;
    ListNode() {

    }
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public void printList() {
        ListNode current = this;
        while (current != null) {
            if (current == this) {
                System.out.print("[" + current.val);
            } else if (current.next == null) {
                System.out.print("," + current.val + "]\n");
            }
            else {
                System.out.print("," + current.val);
            }
            current = current.next;
        }
    }
}

class Solution {
    public ListNode getNthNode(ListNode current, int n) {
        ListNode resNode = current;
        for (int i = 0; i < n; i++) {
            resNode = resNode.next;
        }

        return resNode;
    }
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode end = head;
        ListNode current = head;
        ListNode prev = current;

        while (end.next != null) {
            end = end.next;
        }

        if (head == end) {
            head = null;
        }
        else {
            while (getNthNode(current, n - 1) != end) {
                prev = current;
                current = current.next;
            }
            if (current == head) {
                head = head.next;
            }
            else {
                prev.next = prev.next.next;
            }
        }
        
        return head;
    }
}



public class RemoveNthNode {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        // head.next.next = new ListNode(3);
        // head.next.next.next = new ListNode(4);
        // head.next.next.next.next = new ListNode(5);
        head.printList();

        Solution sol = new Solution();
        sol.removeNthFromEnd(head, 2);
        head.printList();
    }
}
