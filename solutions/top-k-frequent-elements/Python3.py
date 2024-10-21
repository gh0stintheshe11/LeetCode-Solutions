from typing import List
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]