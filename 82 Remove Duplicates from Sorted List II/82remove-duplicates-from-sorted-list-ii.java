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
