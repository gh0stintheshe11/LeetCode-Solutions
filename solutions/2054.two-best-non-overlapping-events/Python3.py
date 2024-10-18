from typing import List
from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()  # Sort by start time
        n = len(events)
        max_value = [0] * (n + 1)

        # Find the max value we can get from the i-th event to the last event
        for i in range(n - 1, -1, -1):
            max_value[i] = max(max_value[i + 1], events[i][2])

        result = 0

        for i, (start, end, value) in enumerate(events):
            # Binary search to find the first event that starts after the current event ends
            idx = bisect_right(events, [end, float('inf'), float('inf')])  # Find next non-overlapping
            result = max(result, value + max_value[idx])

        return result