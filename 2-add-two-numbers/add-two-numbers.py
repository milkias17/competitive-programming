# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1)
        new = new_head

        top = l1
        bottom = l2
        carry = 0

        while top or bottom:
            top_val = top.val if top else 0
            bottom_val = bottom.val if bottom else 0
            tmp = top_val + bottom_val + carry
            cur_sum = tmp % 10
            carry = tmp // 10
            new_node = ListNode(cur_sum)
            new.next = new_node
            new = new.next
            if top:
                top = top.next
            if bottom:
                bottom = bottom.next
        
        if carry:
            new_node = ListNode(carry)
            new.next = new_node
            
        return new_head.next