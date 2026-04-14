"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_ref = {}
        queue = deque()
        queue.append((node, None))
        visited = set()
        
        while queue:
            node, parent = queue.popleft()
            cpy = node_ref.get(node.val, None)
            if not cpy:
                cpy = Node(val=node.val)
            
            if parent:
                parent.neighbors.append(cpy)
                cpy.neighbors.append(parent)
            
            node_ref[node.val] = cpy
            for neighbor in node.neighbors:
                if neighbor.val not in node_ref:
                    queue.append((neighbor, cpy))
        
        return node_ref[1]