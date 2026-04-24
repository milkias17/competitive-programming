class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        queue = deque([[0, 0, 0, 0]])
        visited = set([(0,0,0,0)])
        for deadend in deadends:
            visited.add(tuple(map(int, list(deadend))))


        height = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()

                if "".join(map(str, cur)) == target:
                    return height

                for i in range(len(cur)):
                    dec = (cur[i] - 1 + 10) % 10
                    inc = (cur[i] + 1) % 10
                    tmp_dec = cur.copy()
                    tmp_inc = cur.copy()
                    tmp_dec[i] = dec
                    tmp_inc[i] = inc
                    if tuple(tmp_inc) not in visited:
                        visited.add(tuple(tmp_inc))
                        queue.append(tmp_inc)
                    if tuple(tmp_dec) not in visited:
                        visited.add(tuple(tmp_dec))
                        queue.append(tmp_dec)
                
            height += 1
    

        return -1