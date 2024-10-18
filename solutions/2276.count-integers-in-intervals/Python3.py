from sortedcontainers import SortedDict

class CountIntervals:
    def __init__(self):
        self.intervals = SortedDict()
        self.total_count = 0

    def add(self, left: int, right: int) -> None:
        # Update interval `left` to find overlaps
        it = self.intervals.bisect_left(left)
        if it > 0 and self.intervals.peekitem(it - 1)[1] >= left - 1:
            it -= 1
        
        while it < len(self.intervals) and self.intervals.peekitem(it)[0] <= right + 1:
            start, end = self.intervals.popitem(it)
            left = min(left, start)
            right = max(right, end)
            self.total_count -= end - start + 1
        
        self.intervals[left] = right
        self.total_count += right - left + 1
        
    def count(self) -> int:
        return self.total_count

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()