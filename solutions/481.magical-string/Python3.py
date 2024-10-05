class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        
        s = [1, 2, 2]
        head, tail, num_ones = 2, 3, 1
        
        while tail < n:
            size = s[head]
            num = 2 if s[tail - 1] == 1 else 1
            s.extend([num] * size)
            if num == 1:
                num_ones += size
            head += 1
            tail += size
        
        return num_ones - (tail - n if tail > n and s[n] == 1 else 0)