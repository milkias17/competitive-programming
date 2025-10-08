class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = -1
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            cur = width * h
            if cur > area:
                area = cur
            
            if height[left] > height[right]:
                right -= 1
            elif height[right] >= height[left]:
                left += 1
        
        return area
            