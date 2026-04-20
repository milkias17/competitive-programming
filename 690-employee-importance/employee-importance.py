"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj = {}
        for employee in employees:
            adj[employee.id] = (employee.importance, employee.subordinates)

        stack = [id]
        visited = set()
        count = 0

        while stack:
            cur = stack.pop()
            if cur in visited:
                continue

            importance, subordinates = adj[cur]
            count += importance
            for neigh in subordinates:
                stack.append(neigh)
                
            visited.add(cur)
        
        return count

