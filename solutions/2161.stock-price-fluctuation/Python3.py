from heapq import heappush, heappop

class StockPrice:

    def __init__(self):
        self.mp = {}
        self.maxp = [] # max-heap 
        self.minp = [] # min-heap 
        self.latest = 0 # latest timestamp

    def update(self, timestamp: int, price: int) -> None:
        self.mp[timestamp] = price 
        if self.latest <= timestamp: self.latest = timestamp
        heappush(self.maxp, (-price, timestamp))
        heappush(self.minp, (price, timestamp))

    def current(self) -> int:
        return self.mp[self.latest]

    def maximum(self) -> int:
        while self.mp[self.maxp[0][1]] != -self.maxp[0][0]: heappop(self.maxp)
        return -self.maxp[0][0]

    def minimum(self) -> int:
        while self.mp[self.minp[0][1]] != self.minp[0][0]: heappop(self.minp)
        return self.minp[0][0]