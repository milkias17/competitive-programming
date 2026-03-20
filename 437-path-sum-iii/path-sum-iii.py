# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int, prefix={0: 1}, cur_sum=0) -> int:
        if not root:
            return 0
        
        cur_sum += root.val
        tmp = 0
        if cur_sum - targetSum in prefix:
            tmp += prefix[cur_sum - targetSum]
        prefix[cur_sum] = prefix.get(cur_sum, 0) + 1
        left = self.pathSum(root.left, targetSum, prefix, cur_sum)
        right = self.pathSum(root.right, targetSum, prefix, cur_sum)
        prefix[cur_sum] -= 1
        if prefix[cur_sum] <= 0:
            del prefix[cur_sum]
        
        return tmp + left + right


