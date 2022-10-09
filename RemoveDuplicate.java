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

    ListNode(int[] val) {
        ListNode current = this;
        for (int i = 0; i < val.length; i++) {
            if (i == 0) {
                this.val = val[i];
                continue;
            } else {
                current.next = new ListNode(val[i]);
                current = current.next;
            }
        }
    }

    public void printList() {
        ListNode current = this;
        while (current != null) {
            if (current == this) {
                System.out.print("[" + current.val);
                if (current.next == null) {
                    System.out.print("]\n");
                }
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
    
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;
        ListNode prev = head;

        if (head == null) {
            return head;
        }

        while (current != null && current.next != null && head != null) {
            if (current.val == current.next.val) {
                if (current == head) {
                    while (head != null && head.val == current.val) {
                        head = head.next;
                    }
                    prev = head;
                    current = head;
                } else {
                    int toBeRemovedVal = current.val;
                    while (current != null && current.val == toBeRemovedVal) {
                        current = current.next;
                    }
                    prev.next = current;
                }
            } else {
                prev = current;
                current = current.next;
            }
        }

        return head;
    }
}

public class RemoveDuplicate {
    public static void main(String[] args) {
        // int[] arr = {3, 1, 1, 1, 1};
        // int[] arr = {1, 2, 3, 3, 4, 4, 5};
        int[] arr = {1, 1, 1, 2, 3};
        ListNode head = new ListNode(arr);
        head.printList();

        Solution sol = new Solution();
        sol.deleteDuplicates(head);
        head.printList();
    }
}
