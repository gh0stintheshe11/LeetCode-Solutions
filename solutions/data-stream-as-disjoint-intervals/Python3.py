class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new_interval = [value, value]
        temp = []
        placed = False
        
        for i in range(len(self.intervals)):
            if self.intervals[i][1] + 1 < value:  # Current interval ends before the new interval starts
                temp.append(self.intervals[i])
            elif self.intervals[i][0] - 1 > value:  # Current interval starts after the new interval ends
                if not placed:
                    temp.append(new_interval)
                    placed = True
                temp.append(self.intervals[i])
            else:  # Overlapping intervals
                new_interval[0] = min(new_interval[0], self.intervals[i][0])
                new_interval[1] = max(new_interval[1], self.intervals[i][1])
        
        if not placed:
            temp.append(new_interval)
        
        self.intervals = temp

    def getIntervals(self) -> List[List[int]]:
        return self.intervals