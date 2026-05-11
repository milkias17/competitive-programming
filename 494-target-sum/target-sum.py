class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        memo = [[0 for _ in range(2 * (total + 1))] for _ in range(len(nums) + 1)]
        for rep in range(2 * (total + 1)):
            memo[-1][rep] = 1 if rep == target + total else 0
        
        for i in range(len(nums) - 1, -1, -1):
            for cur_sum in range(2 * (total + 1)):
                count = 0
                if cur_sum - nums[i] >= 0:
                    count += memo[i + 1][cur_sum - nums[i]]
                if cur_sum + nums[i] < 2 * (total + 1):
                    count += memo[i + 1][cur_sum + nums[i]]

                memo[i][cur_sum] = count
        
        return memo[0][total]
            