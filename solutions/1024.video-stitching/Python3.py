from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        end, farthest, cnt, i = 0, 0, 0, 0

        while end < time:
            while i < len(clips) and clips[i][0] <= end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if end == farthest:
                return -1
            end = farthest
            cnt += 1
            
        return cnt