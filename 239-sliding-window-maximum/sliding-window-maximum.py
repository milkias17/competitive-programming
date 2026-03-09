class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        max_val = float("-inf")
        res = []

        for right in range(0, len(nums)):
            while len(queue) > 0 and nums[right] >= nums[queue[-1]]:
                queue.pop()

            queue.append(right)
            
            # print(f"Queue: {queue}")
            if right - left + 1 == k:
                # print(f"In for: {nums[left:right+1]}, max: {nums[queue[0]]}")
                res.append(nums[queue[0]])
                if left == queue[0]:
                    queue.popleft()
                
                left += 1
        
        return res
