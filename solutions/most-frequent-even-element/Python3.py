from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_counts = Counter(num for num in nums if num % 2 == 0)
        
        if not even_counts:
            return -1
        
        most_frequent_even = min(even_counts.items(), key=lambda x: (-x[1], x[0]))[0]
        return most_frequent_even