class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        left = 0
        right = len(nums1) - 1

        while True:
            mid = (left + right) // 2
            ptr = half - mid - 2

            left_1 = nums1[mid] if mid >= 0 else float("-inf")
            right_1 = nums1[mid + 1] if mid + 1 < len(nums1) else float("inf")
            left_2 = nums2[ptr] if ptr >= 0 else float("-inf")
            right_2 = nums2[ptr + 1] if ptr + 1 < len(nums2) else float("inf")

            if left_1 <= right_2 and left_2 <= right_1:
                if total % 2 != 0:
                    return min(right_1, right_2)
                else:
                    return (max(left_1, left_2) + min(right_1, right_2)) / 2
            elif left_1 > right_2:
                right = mid - 1
            else:
                left = mid + 1
        