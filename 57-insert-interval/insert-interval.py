class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = [[start, end] for start, end in intervals if start <= newInterval[0]]
        print(merged)
        if merged and merged[-1][1] >= newInterval[0]:
            merged[-1][1] = max(merged[-1][1], newInterval[1])
        else:
            merged.append(newInterval)

        for i in range(len(merged) - 1, len(intervals)):
            interval = intervals[i]
            if merged and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        
        return merged




