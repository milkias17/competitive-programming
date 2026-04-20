class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        res = [0] * len(nums)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    res[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            while i < len(left):
                res[left[i][1]] += j
                merged.append(left[i])
                i += 1

            merged.extend(right[j:])
            return merged
        
        merge_sort(arr)
        return res

