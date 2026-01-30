# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []
        found = 0
        while stack or cur:
            if cur:
                stack.append(cur)            
                cur = cur.left
                continue
            
            node = stack.pop()
            found += 1
            if found == k:
                return node.val
            
            cur = node.right
