class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        from collections import deque
        positions = [deque() for _ in range(10)]
        
        for i, char in enumerate(s):
            positions[int(char)].append(i)
        
        for char in t:
            digit = int(char)
            if not positions[digit]:
                return False
            
            for smaller in range(digit):
                if positions[smaller] and positions[smaller][0] < positions[digit][0]:
                    return False
            positions[digit].popleft()
        
        return True