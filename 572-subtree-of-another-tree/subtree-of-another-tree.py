# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        
        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p.val != q.val:
            return False
        
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        root_check = self.is_same_tree(root, subRoot)
        left = self.is_same_tree(root.left, subRoot)
        right = self.is_same_tree(root.right, subRoot)
        if root_check or left or right:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)