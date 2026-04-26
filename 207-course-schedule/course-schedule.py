class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)
        
        colors = [0 for i in range(numCourses)]

        def dfs(course):
            colors[course] = 1

            for prerequisite in adj[course]:
                if colors[prerequisite] == 1:
                    return True
                
                if colors[prerequisite] == 0 and dfs(prerequisite):
                    return True
            
            colors[course] = 2
            return False
        
        for course in range(numCourses):
            if colors[course] == 0 and dfs(course):
                return False
        
        return True

                