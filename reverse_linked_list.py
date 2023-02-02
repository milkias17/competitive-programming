from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        repr_str = ""
        cur = self
        while cur:
            if not cur.next:
                repr_str += f"{cur.val}"
            else:
                repr_str += f"{cur.val},"
            cur = cur.next
        return repr_str


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head.next
        prev = head
        prev.next = None
        while cur.next:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        cur.next = prev
        return cur


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next = ListNode(5)
    print(head)
    sol = Solution()
    x = sol.reverseList(head)
    print(x)
