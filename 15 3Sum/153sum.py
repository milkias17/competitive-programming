class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        output = []
        unique_tracker = set()
        for i, o_num in enumerate(sorted_nums[:len(nums) - 2]):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                left_n = sorted_nums[left]
                right_n = sorted_nums[right]
                sum_cur = o_num + left_n + right_n
                if sum_cur == 0:
                    key = "{}{}{}".format(o_num, left_n, right_n)
                    if key not in unique_tracker:
                        output.append([o_num, left_n, right_n])
                        unique_tracker.add(key)
                    
                    left += 1
                    right -= 1
                elif sum_cur > 0:
                    right -= 1
                else:
                    left += 1
        
        return output