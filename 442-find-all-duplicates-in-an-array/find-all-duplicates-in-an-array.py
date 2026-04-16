class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cur = 0
        ans = set()

        while cur < len(nums):
            idx = nums[cur] - 1
            if idx == cur:
                cur += 1
            else:
                if nums[idx] == nums[cur]:
                    ans.add(nums[cur])
                    cur += 1
                    continue

                nums[idx], nums[cur] = nums[cur], nums[idx]
        
        return list(ans)