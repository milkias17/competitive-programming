class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.max_count = 0 

        def dfs(i, taken):
            x, y, r = bombs[i]

            count = 1
            taken.add(i)
            for j, bomb in enumerate(bombs):
                if j in taken:
                    continue
                tx, ty, _ = bomb
                if sqrt(pow(tx - x, 2) + pow(ty - y, 2)) <= r:
                    count += dfs(j, taken)
            
            return count
        
        for i in range(len(bombs)):
            self.max_count = max(self.max_count, dfs(i, set()))
        
        return self.max_count

