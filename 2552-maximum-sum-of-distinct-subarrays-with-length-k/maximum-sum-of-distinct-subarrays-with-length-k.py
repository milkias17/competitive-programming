class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        i = 0
        holder = set()
        cur_sum = 0
        num_els = 0
        while i < len(nums):
            if nums[i] in holder:
                holder.remove(nums[i - num_els])
                cur_sum -= nums[i - num_els]
                num_els -= 1
                continue
            
            holder.add(nums[i])
            cur_sum += nums[i]
            num_els += 1
            if num_els == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[i - k + 1]
                holder.remove(nums[i - k + 1])
                num_els -= 1
            
            i += 1

        return max_sum