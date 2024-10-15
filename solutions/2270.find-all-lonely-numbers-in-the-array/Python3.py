class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter
        
        # Count the occurrences of each number
        num_count = Counter(nums)
        
        lonely_numbers = []
        
        for num in num_count:
            # A number is lonely if it appears once and neither num - 1 nor num + 1 appears in nums
            if num_count[num] == 1 and (num - 1 not in num_count) and (num + 1 not in num_count):
                lonely_numbers.append(num)
        
        return lonely_numbers