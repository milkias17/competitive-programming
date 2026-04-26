class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        in_order = {i: 0 for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            in_order[course] += 1
        
        queue = deque()
        for k, v in in_order.items():
            if v == 0:
                queue.append(k)
        
        res = []
        while queue:
            prerequisite = queue.popleft()
            for course in adj[prerequisite]:
                in_order[course] -= 1
                if in_order[course] <= 0:
                    queue.append(course)
            
            res.append(prerequisite)
        
        return res if len(res) == numCourses else []

