class Solution:
    def backtrack(self, n, k, i, cur_set, power_set):
        if len(cur_set) == k:
            power_set.append(cur_set.copy())
            return
        
        for j in range(i, n + 1):
            cur_set.append(j)
            self.backtrack(n, k, j + 1, cur_set, power_set)
            cur_set.pop()


    def combine(self, n: int, k: int) -> List[List[int]]:
        power_set = []
        self.backtrack(n, k, 1, [], power_set)
        return power_set