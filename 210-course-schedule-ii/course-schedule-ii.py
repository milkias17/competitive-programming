class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
        
        stack = []
        colors = [0] * numCourses

        def dfs(course):
            colors[course] = 1

            for prerequisite in adj[course]:
                if colors[prerequisite] == 1:
                    return False
                
                if colors[prerequisite] == 0 and not dfs(prerequisite):
                    return False
            
            colors[course] = 2
            stack.append(course)
            return True
        
        for course in adj:
            if colors[course] != 0:
                continue
            
            if not dfs(course):
                return []
        
        stack.reverse()
        return stack
