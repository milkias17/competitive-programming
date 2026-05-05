# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        
        pos = k % n
        if pos == 0:
            return head

        slow = head
        fast = head
        for _ in range(pos):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        tmp = slow.next
        slow.next = None
        fast.next = head
        return tmp
