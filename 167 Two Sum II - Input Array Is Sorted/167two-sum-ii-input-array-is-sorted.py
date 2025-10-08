class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_o = numbers[left] + numbers[right]
            if sum_o == target:
                return [left + 1, right + 1]
            if target > sum_o:
                left += 1
            elif target < sum_o:
                right -= 1
        
        return []
            