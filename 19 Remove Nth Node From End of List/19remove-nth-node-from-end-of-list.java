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
