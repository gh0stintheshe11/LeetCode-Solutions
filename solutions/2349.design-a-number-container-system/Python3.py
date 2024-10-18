import collections
import heapq

class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = collections.defaultdict(list)
        self.active_indices = collections.defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if index in self.active_indices[old_number]:
                self.active_indices[old_number].remove(index)
        
        self.index_to_number[index] = number
        heapq.heappush(self.number_to_indices[number], index)
        self.active_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.active_indices or not self.active_indices[number]:
            return -1
        
        while self.number_to_indices[number] and self.number_to_indices[number][0] not in self.active_indices[number]:
            heapq.heappop(self.number_to_indices[number])

        if self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        else:
            return -1