class Solution:
    def playGame(self, nums, start, end):
        if start > end:
            return 0
        
        take_left = nums[start] - self.playGame(nums, start + 1, end)
        take_right = nums[end] - self.playGame(nums, start, end - 1)

        return max(take_left, take_right)
        

    def predictTheWinner(self, nums: List[int]) -> bool:
        score =  self.playGame(nums, 0, len(nums) - 1)
        return score >= 0


        