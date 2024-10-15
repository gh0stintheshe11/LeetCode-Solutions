from sortedcontainers import SortedDict

class RangeModule:

    def __init__(self):
        self.ranges = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        start, end = left, right
        l = self.ranges.bisect_left(left)
        
        if l != 0 and self.ranges.items()[l - 1][1] >= left:
            l -= 1
        
        while l < len(self.ranges) and self.ranges.items()[l][0] <= right:
            start = min(start, self.ranges.items()[l][0])
            end = max(end, self.ranges.items()[l][1])
            self.ranges.popitem(l)
        
        self.ranges[start] = end

    def queryRange(self, left: int, right: int) -> bool:
        l = self.ranges.bisect_right(left)
        if l == 0:
            return False
        return self.ranges.items()[l - 1][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        start, end = left, right
        l = self.ranges.bisect_left(start)
        
        if l != 0 and self.ranges.items()[l - 1][1] > start:
            l -= 1
        
        new_ranges = []
        
        while l < len(self.ranges) and self.ranges.items()[l][0] < end:
            if self.ranges.items()[l][0] < start:
                new_ranges.append((self.ranges.items()[l][0], start))
            if self.ranges.items()[l][1] > end:
                new_ranges.append((end, self.ranges.items()[l][1]))
            self.ranges.popitem(l)
        
        for new_start, new_end in new_ranges:
            self.ranges[new_start] = new_end

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)