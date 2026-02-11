class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        set1 = set(nums1)
        set2 = set(nums2)

        res.append(list(set1.difference(set2)))
        res.append(list(set2.difference(set1)))
        return res