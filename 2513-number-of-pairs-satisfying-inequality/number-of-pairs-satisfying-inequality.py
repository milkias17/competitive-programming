class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [n1 - n2 for n1, n2 in zip(nums1, nums2)]

        seen = []
        res = 0

        for num in arr:
            count = bisect_right(seen, num + diff)
            res += count

            insort(seen, num)
        
        return res