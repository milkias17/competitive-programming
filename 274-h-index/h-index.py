class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_h = 0

        i = 0
        for j in range(1, 1001):
            while i < len(citations) and j > citations[i]:
                i += 1

            if len(citations) - i >= j:
                max_h = max(max_h, j)
            
        return max_h