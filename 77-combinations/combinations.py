class Solution:
    def recurser(self, i, n, k, cur_combs, power_combs):
        if len(cur_combs) == k:
            power_combs.append(cur_combs.copy())
            return
        if i > n:
            return


        for j in range(i, n + 1):
            cur_combs.append(j)
            self.recurser(j + 1, n, k, cur_combs, power_combs)
            cur_combs.pop()
        

    def combine(self, n: int, k: int) -> List[List[int]]:
        cur_combs, power_combs = [], []
        self.recurser(1, n, k, cur_combs, power_combs)
        return power_combs
        