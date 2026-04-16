class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break
        
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return fast