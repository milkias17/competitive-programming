"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        mem = {}
        old_cur = head
        new_head = Node(head.val)
        new_cur = new_head
        while old_cur:
            mem[old_cur] = new_cur
            if old_cur.next:
                new_next = Node(old_cur.next.val)
                new_cur.next = new_next
            old_cur = old_cur.next
            new_cur = new_cur.next

        old_cur = head
        new_cur = new_head
        while old_cur:
            if old_cur.random is not None:
                new_cur.random = mem[old_cur.random]
            old_cur = old_cur.next
            new_cur = new_cur.next
        
        return new_head
