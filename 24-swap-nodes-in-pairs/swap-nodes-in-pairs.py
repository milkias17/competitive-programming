# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        cur = head
        new_head = cur.next
        prev = None
        while cur and cur.next:
            left = cur
            right = cur.next
            nxt = right.next
            right.next = left
            left.next = nxt
            if prev:
                prev.next = right
            prev = left
            cur = nxt
        
        return new_head