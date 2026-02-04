class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        new_intervals = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = new_intervals[-1]
            if start >= prev_start and start <= prev_end:
                new_intervals[-1] = [prev_start, max(end, prev_end)]
            else:
                new_intervals.append([start, end])
        
        return new_intervals

