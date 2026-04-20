class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        red = 0
        white = counter[0]
        blue = white + counter[1]
        t_white = white
        t_blue = blue

        ptr = 0
        while ptr < len(nums) and (red < t_white or white < t_blue or blue < len(nums)):
            cur = nums[ptr]
            should = None
            if cur == 0:
                if red == ptr:
                    red += 1
                    ptr += 1
                else:
                    nums[red], nums[ptr] = nums[ptr], nums[red]
                    while red < len(nums) and nums[red] == 0:
                        red += 1
            elif cur == 1:
                if white == ptr:
                    white += 1
                    ptr += 1
                else:
                    nums[white], nums[ptr] = nums[ptr], nums[white]
                    while white < len(nums) and nums[white] == 1:
                        white += 1
            else:
                if blue == ptr:
                    blue += 1
                    ptr += 1
                else:
                    nums[blue], nums[ptr] = nums[ptr], nums[blue]
                    while blue < len(nums) and nums[blue] == 2:
                        blue += 1
            
