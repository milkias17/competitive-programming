class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        reachables = {i: set() for i in range(numCourses)}
        in_degree = [0 for i in range(numCourses)]

        for prereq, course in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            cur = queue.popleft()

            for neigh in adj[cur]:
                reachables[neigh].update(reachables[cur], set([cur]))
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        
        res = []
        for prereq, course in queries:
            res.append(prereq in reachables[course])
        
        return res

