# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 or list2:
            tmp = None
            if not list1:
                tmp = list2
                list2 = list2.next
                tmp.next = None
            elif not list2 or list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
                tmp.next = None
            else:
                tmp = list2
                list2 = list2.next
                tmp.next = None

            cur.next = tmp
            cur = cur.next

        return dummy.next
