class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            for _range in ranges:
                start, end = _range
                if num >= start and num <= end:
                    break
            else:
                return False
        
        return True