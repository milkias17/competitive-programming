class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        reachables = {i: set() for i in range(numCourses)}

        for prereq, course in prerequisites:
            adj[prereq].append(course)

        visited = set()
        def dfs(course):
            visited.add(course)
            for neigh in adj[course]:
                if neigh in visited:
                    tmp = reachables[neigh].union(set([neigh]))
                    reachables[course].update(tmp)
                else:
                    tmp = dfs(neigh)
                    reachables[course].update(tmp)
            
            return reachables[course].union(set([course]))
                    
        for course in range(numCourses):
            if course not in visited:
                dfs(course)
        
        res = []
        for prereq, course in queries:
            if course in reachables[prereq]:
                res.append(True)
            else:
                res.append(False)
        
        return res
