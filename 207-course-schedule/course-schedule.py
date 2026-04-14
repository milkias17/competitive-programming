class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(0, numCourses)}
        in_degree = {i: 0 for i in range(0, numCourses)}

        for course, req in prerequisites:
            in_degree[course] = in_degree[course] + 1
            adj[req].append(course)
            
        
        queue = deque()
        for k, v in in_degree.items():
            if v == 0:
                queue.append(k)
        
        while queue:
            cur = queue.popleft()
            numCourses -= 1
            for course in adj[cur]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        
        return numCourses == 0


            