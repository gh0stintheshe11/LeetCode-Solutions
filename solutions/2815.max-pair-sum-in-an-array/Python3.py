class Solution:
    def maxSum(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        def largest_digit(num):
            return max(int(d) for d in str(num))
        
        digit_map = defaultdict(list)
        
        for num in nums:
            digit = largest_digit(num)
            digit_map[digit].append(num)
        
        max_sum = -1
        
        for values in digit_map.values():
            if len(values) > 1:
                # Sort descending to get the two largest numbers
                values.sort(reverse=True)
                # Calculate potential max sum
                potential_sum = values[0] + values[1]
                # Update max_sum if this potential_sum is larger
                max_sum = max(max_sum, potential_sum)
        
        return max_sum