from typing import Optional

"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their
nodes contains a single digit. Add the two numbers and return the sum
as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        repr_str = ""
        cur = self
        while cur:
            if not cur.next:
                repr_str += str(cur.val)
            else:
                repr_str += f"{cur.val}, "
            cur = cur.next
        return repr_str


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
