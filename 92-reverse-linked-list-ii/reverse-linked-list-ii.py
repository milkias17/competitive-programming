# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        i = 1
        while i < left:
            cur = cur.next
            i += 1
        
        left_n = cur
        start = cur.next
        left_n.next = None
        prev = None
        nxt = None
        i = left
        tmp = start
        while i <= right:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt
            i += 1
        
        start.next = nxt
        left_n.next = prev
        return dummy.next
        

        