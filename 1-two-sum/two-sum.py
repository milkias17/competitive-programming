class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {num: idx for idx, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if target - num in num_idx and num_idx[target - num] != i:
                return [i, num_idx[target - num]]
