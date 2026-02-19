class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        prefix_right = [-1] * len(nums)
        cur_max = None
        counter = {}
        for i in range(len(nums) - 1, -1, -1):
            if cur_max is None or counter[cur_max] <= (len(nums) - (i + 1)) // 2:
                prefix_right[i] = -1
            else:
                prefix_right[i] = cur_max
            
            counter[nums[i]] = counter.get(nums[i], 0) + 1
            if not cur_max:
                cur_max = nums[i]
            elif counter[nums[i]] > counter[cur_max]:
                cur_max = nums[i]
        
        counter = {}
        cur_max = None
        for i in range(len(nums)):
            if prefix_right[i] == -1:
                continue

            counter[nums[i]] = counter.get(nums[i], 0) + 1
            if not cur_max:
                cur_max = nums[i]
            elif counter[nums[i]] > counter[cur_max]:
                cur_max = nums[i]

            if counter[cur_max] > (i + 1) // 2 and cur_max == prefix_right[i]:
                return i

        return -1
