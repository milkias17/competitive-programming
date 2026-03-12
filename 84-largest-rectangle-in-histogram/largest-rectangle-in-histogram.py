class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                idx = stack.pop()
                end_idx = i - 1
                start_idx = stack[-1] + 1 if stack else 0
                width = end_idx - start_idx + 1
                max_area = max(max_area, width * heights[idx])
            
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            end_idx = len(heights) - 1
            start_idx = stack[-1] + 1 if stack else 0
            width = end_idx - start_idx + 1
            height = heights[idx]
            max_area = max(max_area, width * height)
        
        return max_area
            