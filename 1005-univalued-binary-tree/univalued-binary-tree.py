# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        num = root.val

        while queue:
            cur = queue.pop()
            if cur.val != num:
                return False
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return True
