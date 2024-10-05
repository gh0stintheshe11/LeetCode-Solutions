from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each value
        freq = Counter(nums)
        
        # Step 2: Sort the array with a custom comparator
        # The key for sorting will be a tuple (frequency, -value)
        # This ensures that we sort by frequency first (ascending) and by value second (descending)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums