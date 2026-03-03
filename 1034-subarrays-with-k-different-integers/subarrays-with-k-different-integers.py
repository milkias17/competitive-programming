class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        f_left = 0
        left = 0
        counter = Counter()
        count = 0

        for right in range(len(nums)):
            counter[nums[right]] += 1
            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] <= 0:
                    del counter[nums[left]]
                left += 1
                f_left = left
            
            while counter[nums[left]] > 1:
                counter[nums[left]] -= 1
                left += 1

            if len(counter) == k:
                count += (left - f_left) + 1

        
        return count