class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        prev_holder = {}
        tasks_heap = []
        for task in tasks:
            priority = 0
            if task in prev_holder:
                priority = prev_holder[task] + n + 1

            prev_holder[task] = priority
            tasks_heap.append((priority, task))
        
        heapify(tasks_heap)
        cur_interval = 0
        while tasks_heap:
            if tasks_heap[0][0] <= cur_interval:
                heappop(tasks_heap)

            cur_interval += 1
        
        return cur_interval
