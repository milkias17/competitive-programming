# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        
        def dfs(node):
            if not node:
                return (True, float("inf"), float("-inf"), 0)
            
            l_b, l_min, l_max, l_sum = dfs(node.left)
            r_b, r_min, r_max, r_sum = dfs(node.right)

            if not l_b or not r_b:
                return (False, min(l_min, r_min), max(l_max, r_max), l_sum)
            
            if node.val <= l_max or node.val >= r_min:
                return (False, l_min, l_max, l_sum)
            
            self.max_val = max(self.max_val, l_sum + r_sum + node.val)
            return True, min(l_min, r_min, node.val), max(l_max, r_max, node.val), l_sum + r_sum + node.val
        
        dfs(root)
        return self.max_val
            




