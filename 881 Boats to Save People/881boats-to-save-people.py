class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left_pointer = 0
        right_pointer = len(people) - 1
        num_boats = 0
        people = sorted(people, reverse=True)

        while left_pointer <= right_pointer:            
            if people[left_pointer] + people[right_pointer] <= limit:
                left_pointer += 1
                right_pointer -= 1
                num_boats += 1
            else:
                left_pointer += 1
                num_boats += 1
        
        return num_boats
