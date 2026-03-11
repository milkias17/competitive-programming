# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        queue = deque()
        dummy = ListNode(val=float("inf"), next=head)
        queue.append(dummy)

        cur = head
        while cur:
            while queue and cur.val > queue[-1].val:
                queue.pop()
            queue[-1].next = cur
            queue.append(cur)
            cur = cur.next
        
        return dummy.next