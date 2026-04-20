# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, path):
            if not node:
                return 0
            
            count = 0
            if len(path) >= 2 and path[-2] % 2 == 0:
                count += node.val

            path.append(node.val)
            if node.left:
                count += dfs(node.left, path)
            if node.right:
                count += dfs(node.right, path)

            path.pop()
            return count
        
        return dfs(root, [])