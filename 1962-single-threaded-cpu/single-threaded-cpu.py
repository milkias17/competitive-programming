class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        tasks = [[task[0], task[1], i] for i, task in enumerate(tasks)]
        tasks.sort()

        heappush(heap, (tasks[0][1], tasks[0][2], 0))
        
        res = []
        cur_time = tasks[0][0]
        cur = 1
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