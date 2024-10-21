class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count_digit(x, d):
            if x < 0:
                return 0
            s = str(x)
            n = len(s)
            total_count = 0
            
            for i in range(n):
                current = int(s[i])
                left_part = int(s[:i]) if i > 0 else 0
                right_part = int(s[i+1:]) if i < n-1 else 0
                position_weight = 10 ** (n-i-1)
                
                total_count += left_part * position_weight
                
                if current > d:
                    total_count += position_weight
                elif current == d:
                    total_count += right_part + 1
                
                if d == 0:
                    total_count -= position_weight
        
            return total_count
        
        return count_digit(high, d) - count_digit(low-1, d)