class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        max_queue = deque()
        min_val = None
        for i, num in enumerate(nums):
            while max_queue and max_queue[-1][0] <= num:
                max_queue.pop()
            if max_queue and max_queue[-1][1] is not None and num > max_queue[-1][1]:
                return True

            if min_val is None or num < min_val:
                min_val = num
            max_queue.append((num, min_val))
        
        return False
            


