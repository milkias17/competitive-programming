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
        mapper = {}
        copy_head = Node(-1)
        copy = copy_head

        cur = head
        while cur:
            new_node = Node(cur.val, random=cur.random)
            mapper[cur] = new_node
            copy.next = new_node
            copy = copy.next
            cur = cur.next
        
        cur = copy_head
        while cur:
            if cur.random is not None:
                cur.random = mapper[cur.random]
            cur = cur.next

        return copy_head.next