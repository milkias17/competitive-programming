class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        max_len = 0
        left = 0

        for i, num in enumerate(nums):
            while max_queue and nums[max_queue[-1]] < num:
                max_queue.pop()
            max_queue.append(i)
            
            while min_queue and nums[min_queue[-1]] > num:
                min_queue.pop()
            min_queue.append(i)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if max_queue[0] == left:
                    max_queue.popleft()
                if min_queue[0] == left:
                    min_queue.popleft()
                left += 1
            
            max_len = max(max_len, i - left + 1)
        
        return max_len




            