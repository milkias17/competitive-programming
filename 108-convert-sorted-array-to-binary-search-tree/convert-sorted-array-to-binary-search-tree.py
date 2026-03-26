# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int], start=0, end=None) -> Optional[TreeNode]:
        if end is None:
            end = len(nums) - 1

        if start > end:
            return None

        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums, start, mid - 1)
        root.right = self.sortedArrayToBST(nums, mid + 1, end)

        return root