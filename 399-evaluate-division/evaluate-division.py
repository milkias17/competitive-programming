class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, equation in enumerate(equations):
            var1, var2 = equation
            res = values[i]
            adj[var1].append((var2, res))
            adj[var2].append((var1, 1 / res))
        
        def dfs(cur, end, total, visited):
            if cur == end:
                return total
            
            visited.add(cur)

            for neigh, weight in adj[cur]:
                if neigh in visited:
                    continue
                res = dfs(neigh, end, total * weight, visited)
                if res != -1:
                    return res
            
            return -1.0

        output = []
        for start, end in queries:
            if start not in adj or end not in adj:
                output.append(-1.0)
                continue

            res = dfs(start, end, 1.0, set())
            output.append(res)            
        
        return output
