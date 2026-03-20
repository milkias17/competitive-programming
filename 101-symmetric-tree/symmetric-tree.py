# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, t1, t2):
        if not t1 and not t2:
            return True
        
        if not t1 and t2 or not t2 and t1:
            return False
        
        if t1.val != t2.val:
            return False
        
        return self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)
        