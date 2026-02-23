class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            cur_height = min(height[right], height[left])
            max_area = max(max_area, width * cur_height)

            if cur_height == height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area