from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        
        def neighbors(s):
            i = 0
            while s[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(s)):
                if s[j] == s2[i]:
                    yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
        
        queue = deque([(s1, 0)])
        visited = {s1}
        
        while queue:
            s, k = queue.popleft()
            for neighbor in neighbors(s):
                if neighbor in visited:
                    continue
                if neighbor == s2:
                    return k + 1
                visited.add(neighbor)
                queue.append((neighbor, k + 1))
        
        return -1