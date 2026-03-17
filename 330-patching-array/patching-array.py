class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        end = 0
        count = 0
        i = 0

        while end < n and i < len(nums):
            num = nums[i]
            print(f"Cur range: [0, {end}]")

            if num <= end + 1:
                end += num
                i += 1
            else:
                count += 1
                end += end + 1
        
        while end < n:
            end += end + 1
            count += 1

        return count