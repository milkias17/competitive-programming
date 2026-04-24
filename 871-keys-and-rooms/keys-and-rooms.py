class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque([0])
        count = 0
        visited = set([0])

        while queue:
            cur_room = queue.popleft()
            count += 1

            for key in rooms[cur_room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        
        return count == len(rooms)
