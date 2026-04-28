class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        stack = []
        colors = [0 for i in range(numCourses)]

        def dfs(cur):
            colors[cur] = 1

            for neigh in adj[cur]:
                if colors[neigh] == 1:
                    return False
                if colors[neigh] != 2 and not dfs(neigh):
                    return False
            

            stack.append(cur)
            colors[cur] = 2
            return True
        
        for i in range(numCourses):
            if colors[i] == 0 and not dfs(i):
                return []
        
        return stack[::-1]
                