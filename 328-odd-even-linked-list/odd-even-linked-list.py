# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head                
        
        tail = head
        count = 1
        while tail.next:
            tail = tail.next
            count += 1
        
        if count <= 2:
            return head


        cur = head.next
        prev = head

        tmp = count // 2 if count % 2 == 0 else (count - 1) // 2
        while cur and tmp > 0:
            prev.next = cur.next
            prev = cur.next
            nxt = cur.next.next if cur.next else None
            tail.next = cur
            tail = cur
            tail.next = None
            cur = nxt
            tmp -= 1
        
        return head

                

        