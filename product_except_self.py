from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left = []
        prefix_right = [0] * len(nums)

        prefix_left.append(nums[0])
        for i in range(1, len(nums)):
            prefix_left.append(prefix_left[i - 1] * nums[i])

        prefix_right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            prefix_right[i] = prefix_right[i + 1] * nums[i]

        output = []
        for i in range(len(nums)):
            res = 0
            if i == 0:
                res = prefix_right[i + 1]
            elif i == len(nums) - 1:
                res = prefix_left[i - 1]
            else:
                res = prefix_left[i - 1] * prefix_right[i + 1]
            output.append(res)

        return output
