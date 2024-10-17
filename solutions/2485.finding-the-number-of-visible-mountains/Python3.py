from typing import List
from collections import deque

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        peaks = sorted(peaks, key=lambda p: p[0])
        queue = deque()
        prepop = None
        for i in range(len(peaks) - 1, -1, -1):
            peak = peaks[i]
            if len(queue) == 0 and peak != prepop:
                queue.appendleft(peaks[i])
                continue

            while len(queue) > 0 and peak:
                top = queue[0]
                if peak == top:
                    prepop = queue.popleft() 
                    peak = None
                    break

                # check if top is within peak
                l = peak[1] - top[1]
                if peak[0] - l <= top[0] <= peak[0] + l:
                    prepop = queue.popleft()
                else:
                    l = top[1] - peak[1]
                    if not top[0] - l <= peak[0] <= top[0] + l:
                        queue.appendleft(peak)
                        
                    peak = None
            
            if peak and peak != prepop:
                queue.appendleft(peak)

        return len(queue)