# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], acc=0) -> int:
        queue = deque()
        if root:
            queue.append((root, 1))
        height = 0

        while queue:
            cur, h = queue.popleft()
            if cur.left:
                queue.append((cur.left, h + 1))
            if cur.right:
                queue.append((cur.right, h + 1))
            
            height = h

        return height

