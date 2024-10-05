from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        queue = deque()
        result = []
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            queue.append((char, freq + 1))
            
            if len(queue) < k:
                continue
            
            char, freq = queue.popleft()
            if -freq > 0:
                heapq.heappush(max_heap, (freq, char))
        
        return "".join(result) if len(result) == len(s) else ""