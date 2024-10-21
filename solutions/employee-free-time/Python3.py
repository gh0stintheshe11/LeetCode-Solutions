# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Flatten the list of schedules and collect all intervals
        intervals = [interval for employee in schedule for interval in employee]
        
        # Sort the intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        # Array to hold the merged intervals
        merged = [intervals[0]]
        
        # Merge overlapping intervals
        for interval in intervals[1:]:
            if interval.start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, interval.end)
            else:
                merged.append(interval)
                
        # Find the gaps between the merged intervals
        free_times = []
        for i in range(1, len(merged)):
            free_times.append(Interval(merged[i-1].end, merged[i].start))
        
        return free_times