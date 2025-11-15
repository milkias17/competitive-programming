class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = {0: 0, 1: 0}
        for student in students:
            counter[student] = counter.get(student, 0) + 1
        
        while len(students) > 0:
            if students[0] == sandwiches[0]:
                counter[students[0]] -= 1
                students.pop(0)
                sandwiches.pop(0)
                continue
            
            if counter[sandwiches[0]] == 0:
                break
            
            tmp = students.pop(0)
            students.append(tmp)
        
        return len(students)
            
            
