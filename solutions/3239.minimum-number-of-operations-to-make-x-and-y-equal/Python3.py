from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x == y:
            return 0
        
        operations = [(11, lambda x: x // 11), (5, lambda x: x // 5)]
        visited = set()
        queue = deque([(x, 0)])
        
        while queue:
            current, ops = queue.popleft()
            for mod, operation in operations:
                if current % mod == 0:
                    next_val = operation(current)
                    if next_val == y:
                        return ops + 1
                    if next_val not in visited:
                        visited.add(next_val)
                        queue.append((next_val, ops + 1))
            
            if current - 1 == y or current + 1 == y:
                return ops + 1
            if current - 1 not in visited:
                visited.add(current - 1)
                queue.append((current - 1, ops + 1))
            if current + 1 not in visited:
                visited.add(current + 1)
                queue.append((current + 1, ops + 1))
        
        return abs(x - y)