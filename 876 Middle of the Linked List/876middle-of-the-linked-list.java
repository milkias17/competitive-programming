/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        int size = 0;
        ListNode current = head;
        int midIndex = 0;

        while (current != null) {
            size++;
            current = current.next;
        }
        if (size % 2 == 0) {
            midIndex = (size + 1) / 2;
        } else {
            midIndex = size / 2;
        }

        current = head;
        for (int i = 0; i < midIndex; i++) {
            current = current.next;
        }

        return current;
    }
}