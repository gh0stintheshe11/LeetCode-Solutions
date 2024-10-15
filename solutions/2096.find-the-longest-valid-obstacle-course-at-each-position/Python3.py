from typing import List
import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        result = []
        
        for obs in obstacles:
            idx = bisect.bisect_right(lis, obs)
            if idx == len(lis):
                lis.append(obs)
            else:
                lis[idx] = obs
            result.append(idx + 1)
        
        return result