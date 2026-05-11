class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(map(int, list("".join(map(str, nums)))))