# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        left = head
        right = prev
        while right:
            tmp1, tmp2 = left.next, right.next
            left.next, right.next = right, tmp1
            left, right = tmp1, tmp2
            

