import collections
import heapq

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream = collections.deque()
        self.sorted_list = []  # This will maintain the sorted order of the last m elements.
        self.total_sum = 0
    
    def _insert_sorted(self, num: int):
        # Binary search insert
        low, high = 0, len(self.sorted_list)
        while low < high:
            mid = (low + high) // 2
            if self.sorted_list[mid] < num:
                low = mid + 1
            else:
                high = mid
        self.sorted_list.insert(low, num)

    def _remove_sorted(self, num: int):
        # Binary search remove
        low, high = 0, len(self.sorted_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.sorted_list[mid] == num:
                self.sorted_list.pop(mid)
                return
            elif self.sorted_list[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
    
    def addElement(self, num: int) -> None:
        if len(self.stream) == self.m:
            oldest = self.stream.popleft()
            self.total_sum -= oldest
            self._remove_sorted(oldest)

        self.stream.append(num)
        self.total_sum += num
        self._insert_sorted(num)

    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m:
            return -1
        
        trimmed_sum = self.total_sum
        trimmed_sum -= sum(self.sorted_list[:self.k])
        trimmed_sum -= sum(self.sorted_list[-self.k:])
        return trimmed_sum // (self.m - 2 * self.k)