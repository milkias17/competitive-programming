class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        tasks = [[task[0], task[1], i] for i, task in enumerate(tasks)]
        tasks.sort()

        heappush(heap, (tasks[0][1], tasks[0][2], 0))
        cur = 1
        for i in range(1, len(tasks)):
            if tasks[i][0] == tasks[0][0]:
                heappush(heap, (tasks[i][1], tasks[i][2], i))
                cur = i + 1
            else:
                cur = i
                break
        
        res = []
        cur_time = 1
        while heap:
            process_time, org, i = heappop(heap)
            if tasks[i][0] > cur_time:
                cur_time = tasks[i][0]
            
            cur_time += process_time
            res.append(org)

            while cur < len(tasks) and tasks[cur][0] <= cur_time:
                heappush(heap, (tasks[cur][1], tasks[cur][2], cur))
                cur += 1
            
            if not heap and cur < len(tasks):
                heappush(heap, (tasks[cur][1], tasks[cur][2], cur))
                cur += 1
        
        return res