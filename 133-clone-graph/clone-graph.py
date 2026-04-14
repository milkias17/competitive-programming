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

        node_ref = {node: Node(node.val)}
        queue = deque()
        queue.append(node)
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in node_ref:
                    node_ref[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                node_ref[curr].neighbors.append(node_ref[neighbor])

        return node_ref[node]