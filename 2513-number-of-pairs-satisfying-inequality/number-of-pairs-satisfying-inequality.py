class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        self.count = 0

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            i = 0
            for j in range(len(right)):
                while i < len(left) and left[i] <= right[j] + diff:
                    i += 1
                self.count += i
            
            return sorted(left + right)
        
        merge_sort(arr)
        return self.count
