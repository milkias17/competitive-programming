class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        idx = 0
        for color in [0, 1, 2]:
            for _ in range(counter[color]):
                nums[idx] = color
                idx += 1
