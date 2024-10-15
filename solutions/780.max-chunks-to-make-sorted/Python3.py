from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_element = 0
        chunks = 0
        for i in range(len(arr)):
            max_element = max(max_element, arr[i])
            if max_element == i:
                chunks += 1
        return chunks