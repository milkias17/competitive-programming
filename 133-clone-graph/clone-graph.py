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
        node_map = {}
        
        def dfs(cur):
            if not cur:
                return None
                
            if cur in node_map:
                return node_map[cur]
            
            clone = Node(cur.val)
            node_map[cur] = clone
            for neighbor in cur.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
