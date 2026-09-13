class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0

        while queue:
            prereq = queue.popleft()
            count += 1
            for course in adj[prereq]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        
        return count == numCourses

            
