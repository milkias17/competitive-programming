# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        
        pos = k % n
        if pos == 0:
            return head

        slow = head
        fast = head
        for i in range(pos):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        prev = None
        cur = slow.next
        slow.next = None
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        slow.next = prev

        new_head = head
        while slow.next:
            tmp = slow.next
            slow.next = tmp.next
            tmp.next = new_head
            new_head = tmp
        
        return new_head