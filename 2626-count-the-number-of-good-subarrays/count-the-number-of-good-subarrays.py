class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = {}
        cur_k = 0
        left = 0
        count = 0
        for right in range(len(nums)):
            counter[nums[right]] = counter.get(nums[right], 0) + 1
            if counter[nums[right]] > 1:
                cur_k += counter[nums[right]] - 1
                while cur_k >= k:
                    count += 1
                    count += len(nums) - right - 1
                        
                    if counter[nums[left]] > 1:
                        cur_k -= (counter[nums[left]] - 1)
                    counter[nums[left]] -= 1
                    left += 1
        
        return count