class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.longest = 0
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        
        if self.size[p1] >= self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
            if self.size[self.longest] < self.size[p1]:
                self.longest = p1
        elif self.size[p2] > self.size[p1]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
            if self.size[self.longest] < self.size[p2]:
                self.longest = p2
        
        return True



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        uf = UnionFind(len(nums))
        num_idx = {num: i for i, num in enumerate(nums)}

        for num, i in num_idx.items():
            if num - 1 in num_idx:
                uf.union(i, num_idx[num - 1])

            if num not in num_idx:
                num_idx[num] = i
            
        
        return uf.size[uf.longest]