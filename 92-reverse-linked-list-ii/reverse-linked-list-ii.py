# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        
        cur = prev.next
        tmp_prev = None
        nxt = None
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = tmp_prev
            tmp_prev = cur
            cur = nxt

        prev.next.next = nxt
        prev.next = tmp_prev

        return dummy.next