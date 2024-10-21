from typing import List
import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        i = 0
        eaten = 0

        while i < len(apples) or heap:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(heap, (i + days[i], apples[i]))
            while heap and (heap[0][0] <= i or heap[0][1] == 0):
                heapq.heappop(heap)
            if heap:
                expire, count = heapq.heappop(heap)
                if count > 0:
                    eaten += 1
                    count -= 1
                    if count > 0:
                        heapq.heappush(heap, (expire, count))
            i += 1

        return eaten