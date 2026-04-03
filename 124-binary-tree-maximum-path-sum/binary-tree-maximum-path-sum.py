# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")

        def dfs(node):
            if not node:
                return float("-inf")
            
            left = dfs(node.left)
            self.max_path_sum = max(self.max_path_sum, left)
            print(f"Left for: {node.val}, is: {left}")
            right = dfs(node.right)
            self.max_path_sum = max(self.max_path_sum, right)
            print(f"Right for: {node.val}, is: {right}")
    
            total = node.val
            if left >= 0:
                total += left
            if right >= 0:
                total += right
            
            print(f"Total: {total} for {node.val}")
            self.max_path_sum = max(self.max_path_sum, total)
            return node.val + max(max(left, right), 0)
        
        dfs(root)
        return self.max_path_sum
