# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        head = ListNode()
        if not list2:
            head.next = list1
            head.next.next = self.mergeTwoLists(list1.next, list2)
        elif not list1:
            head.next = list2
            head.next.next = self.mergeTwoLists(list1, list2.next)
        elif list1.val <= list2.val:
            head.next = list1
            head.next.next = self.mergeTwoLists(list1.next, list2)
        else:
            head.next = list2
            head.next.next = self.mergeTwoLists(list1, list2.next)

        return head.next