from typing import List
from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [0]
        
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        answer = []
        for query in queries:
            answer.append(bisect_right(prefix_sum, query) - 1)
        
        return answer