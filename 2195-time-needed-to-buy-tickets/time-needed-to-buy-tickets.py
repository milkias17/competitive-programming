class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = tickets.copy()
        cur_idx = k
        time_taken = 0

        while len(queue) > 0:          
            time_taken += 1
            queue[0] -= 1
            tmp = queue.pop(0)
            if tmp == 0:
                if cur_idx == 0:
                    break
                else:
                    cur_idx -= 1
                    continue
            queue.append(tmp)
            cur_idx = len(queue) - 1 if cur_idx == 0 else cur_idx - 1

        
        return time_taken
