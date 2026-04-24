class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = {idx: [] for idx in range(len(bombs))}

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                
                x2, y2, r2 = bombs[j]
                distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
                if distance <= r1:
                    adj[i].append(j)
        
        max_count = 0
        def dfs(node, visited):
            visited.add(node)
            count = 1
            for neigh in adj[node]:
                if neigh in visited:
                    continue

                count += dfs(neigh, visited)
            
            return count
        
        for i in range(len(bombs)):
            max_count = max(max_count, dfs(i, set()))
        
        return max_count
