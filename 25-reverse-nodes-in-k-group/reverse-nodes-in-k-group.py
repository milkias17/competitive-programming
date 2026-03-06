# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseK(self, head, k):
        start = head.next
        head.next = None
        prev = None
        nxt = None
        cur = start
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        head.next = prev
        start.next = nxt
        return start

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        dummy = ListNode(next=head)
        cur = dummy
        for i in range(size // k):
            cur = self.reverseK(cur, k)
        
        return dummy.next


