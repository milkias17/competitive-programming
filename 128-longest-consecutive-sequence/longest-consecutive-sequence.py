class Solution:
    def find(self, parent, val):
        if parent[val] != val:
            parent[val] = self.find(parent, parent[val])

        return parent[val]

    def union(self, nums, parent, val1, val2):
        root1 = self.find(parent, val1)
        root2 = self.find(parent, val2)

        if root1 != root2:
            parent[root2] = root1
            self.size[root1] += self.size[root2]

    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {val: val for idx, val in enumerate(nums)}
        self.size = {val: 1 for val in nums}
        for num in nums:
            if num + 1 in parent:
                self.union(nums, parent, num, num + 1)
        
        if len(self.size) == 0:
            return 0

        return max(self.size.values())