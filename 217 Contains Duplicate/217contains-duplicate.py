class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        holder = {}
        for num in nums:
            if holder.get(num) is None:
                holder[num] = True
            else:
                return True
        return False