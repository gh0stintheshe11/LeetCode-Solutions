from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            freq = Counter(subarray)
            most_common = freq.most_common()
            most_common.sort(key=lambda pair: (-pair[1], -pair[0]))
            
            top_x_elements = set()
            for value, count in most_common[:x]:
                top_x_elements.add(value)

            x_sum = sum(value for value in subarray if value in top_x_elements)
            result.append(x_sum)
        
        return result