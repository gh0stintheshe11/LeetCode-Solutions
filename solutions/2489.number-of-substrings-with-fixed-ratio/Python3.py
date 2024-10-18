class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        from collections import defaultdict
        
        count = 0
        prefix_count_map = defaultdict(int)
        prefix_count_map[0] = 1
        
        zero_count = 0
        one_count = 0
        
        for char in s:
            if char == '0':
                zero_count += 1
            else:
                one_count += 1
            
            # Solve the equation Func(R) * (num1 + num2) - R * num1
            key = zero_count * num2 - one_count * num1
            
            # Use hashmap to find how many such L exist
            if key in prefix_count_map:
                count += prefix_count_map[key]
            
            # Update hashmap with current position
            prefix_count_map[key] += 1
        
        return count