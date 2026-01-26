# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left = dummy
        prev = dummy
        cur = head
        while cur:
            if cur.val < x:
                prev.next = cur.next
                cur.next = left.next
                left.next = cur
                left = cur
            prev = cur
            cur = cur.next
        
        return dummy.next