class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = []
        for row in grid:
            flat.extend(row)
        
        flat.sort()
        mid = len(flat) // 2
        median = flat[mid]
        if any(flat[i] % x != flat[i + 1] % x for i in range(len(flat) - 1)):
            return - 1
        
        ops = 0
        for num in flat:
            ops += abs(median - num) // x

        return ops