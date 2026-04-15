# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left < 0:
                moves += abs(left)
            if right < 0:
                moves += abs(right)

            new_val = node.val + left + right - 1
            if new_val >= 0:
                moves += new_val
            return new_val
        
        dfs(root)
        return moves
            
            
