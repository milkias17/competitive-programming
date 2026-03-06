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
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        
        tmp = (size // 2) - 1 if size % 2 == 0 else (size // 2)
        i = 0
        cur = head
        while i < tmp:
            cur = cur.next
            i += 1
        
        half = cur.next
        cur.next = None

        prev = None
        nxt = None
        cur = half
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        half = prev
        cur = head
        while cur and half:
            tmp = half
            half = half.next
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
