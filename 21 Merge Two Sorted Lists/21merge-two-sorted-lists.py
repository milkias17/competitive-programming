# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        
        
        new_list = ListNode()
        if list1.val <= list2.val:
            new_list.val = list1.val
            list1 = list1.next
        else:
            new_list.val = list2.val
            list2 = list2.next
        
        new_head = new_list
        while list1 or list2:
            if list1 and not list2:
                new_list.next = ListNode(list1.val)
                list1 = list1.next
            elif list2 and not list1:
                new_list.next = ListNode(list2.val)
                list2 = list2.next
            elif list1.val <= list2.val:
                new_list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                new_list.next = ListNode(list2.val)
                list2 = list2.next
            new_list = new_list.next
        
        return new_head