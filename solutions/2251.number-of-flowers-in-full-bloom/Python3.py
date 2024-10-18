from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_times = sorted(flower[0] for flower in flowers)
        end_times = sorted(flower[1] for flower in flowers)
        
        result = []
        for person in people:
            started = bisect_right(start_times, person)
            ended = bisect_left(end_times, person)
            result.append(started - ended)
        
        return result