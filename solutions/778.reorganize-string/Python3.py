from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(max_heap)
        
        prev_count, prev_char = 0, ''
        result = []
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            count += 1
            prev_count, prev_char = count, char
        
        result = ''.join(result)
        if len(result) != len(s):
            return ""
        return result