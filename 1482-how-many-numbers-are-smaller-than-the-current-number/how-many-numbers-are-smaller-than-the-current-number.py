class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        counter = {}
        for i, num in enumerate(sorted_nums):
            if num in counter:
                continue
            counter[num] = i

        answer = [counter[num] for num in nums]
        return answer