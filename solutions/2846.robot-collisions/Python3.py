from typing import List
from operator import mul
from collections import deque

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        healths = map(mul, (-1 if ch == 'L' else 1 for ch in directions), healths)
        arr = sorted(enumerate(healths), key=lambda x: positions[x[0]])
        
        stack = deque([arr.pop(0)])
        
        for idx, hth in arr:
            if hth > 0:
                stack.append((idx, hth))
            else:
                while stack and stack[-1][1] > 0 and hth < 0:
                    IDX, HTH = stack.pop()
                    diff = HTH + hth

                    if diff > 0:
                        idx, hth = IDX, HTH - 1
                    elif diff < 0:
                        hth += 1
                    else:
                        break
                else:
                    stack.append((idx, hth))
                    
        return [abs(hth) for _, hth in sorted(stack)]