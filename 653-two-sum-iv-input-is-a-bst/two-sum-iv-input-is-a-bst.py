# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int, cur_path=None) -> bool:
        if cur_path is None:
            cur_path = set()
            
        if not root:
            return False
        
        if k - root.val in cur_path:
            return True
        
        cur_path.add(root.val)
        return self.findTarget(root.left, k, cur_path) or self.findTarget(root.right, k, cur_path)

