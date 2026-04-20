class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        path = set()

        adj = {course: [] for course in range(numCourses)}
        for start, end in prerequisites:
            adj[end].append(start)

        def dfs(cur):
            if cur in path:
                return False
            if cur in visited:
                return True
            
            visited.add(cur)
            path.add(cur)
            for neighbor in adj[cur]:
                if not dfs(neighbor):
                    return False
            
            path.remove(cur)
            return True
        
        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i):
                return False
        
        return True