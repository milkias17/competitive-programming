# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        adder = 0
        i = 0
        cur = l1
        while cur:
            adder += pow(10, i) * cur.val
            i += 1
            cur = cur.next
        i = 0
        cur = l2
        while cur:
            adder += pow(10, i) * cur.val
            i += 1
            cur = cur.next
        
        str_sum = str(adder)
        head = ListNode(int(str_sum[-1]))
        cur = head
        for n in reversed(str_sum[:len(str_sum) - 1]):
            new_node = ListNode(int(n))
            cur.next = new_node
            cur = new_node
        
        return head