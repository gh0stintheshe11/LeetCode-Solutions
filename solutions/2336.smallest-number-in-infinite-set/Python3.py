import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.available = set()
        self.min_heap = []
        self.next_smallest = 1

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.available.remove(smallest)
            return smallest
        else:
            self.next_smallest += 1
            return self.next_smallest - 1

    def addBack(self, num: int) -> None:
        if num < self.next_smallest and num not in self.available:
            heapq.heappush(self.min_heap, num)
            self.available.add(num)