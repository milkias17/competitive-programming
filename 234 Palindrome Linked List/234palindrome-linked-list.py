# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linked_list = []
        current = head
        while current:
            linked_list.append(current.val)
            current = current.next
        
        leftPointer = 0
        rightPointer = len(linked_list) - 1
        
        while leftPointer <= rightPointer:
            if (linked_list[leftPointer] != linked_list[rightPointer]):
                return False
            leftPointer += 1
            rightPointer -= 1
            
        return True