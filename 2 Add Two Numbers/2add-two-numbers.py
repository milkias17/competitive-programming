# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        
        current = l1
        while current:
            list1.append(current.val)
            current = current.next
        
        current = l2
        while current:
            list2.append(current.val)
            current = current.next

        sum = 0
        for i, j in enumerate(list1):
            sum += j * pow(10, i)
            
        for i, j in enumerate(list2):
            sum += j * pow(10, i)
        
        current = ListNode(sum % 10)
        sum = sum // 10
        head = current
        while sum > 0:
            tmp = ListNode(sum % 10)
            current.next = tmp
            sum = sum // 10
            current = tmp
        
        return head
        
            
        