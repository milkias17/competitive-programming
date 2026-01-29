# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [(root, 1)]
        max_depth = 1
        while queue:
            cur = queue.pop(0)
            max_depth = max(max_depth, cur[1])
            if cur[0].left:
                queue.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                queue.append((cur[0].right, cur[1] + 1))
        
        return max_depth
