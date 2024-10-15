class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1] * n
        i2 = i3 = i5 = 0
        next2, next3, next5 = 2, 3, 5
        
        for k in range(1, n):
            ugly_numbers[k] = min(next2, next3, next5)
            
            if ugly_numbers[k] == next2:
                i2 += 1
                next2 = ugly_numbers[i2] * 2
            
            if ugly_numbers[k] == next3:
                i3 += 1
                next3 = ugly_numbers[i3] * 3
            
            if ugly_numbers[k] == next5:
                i5 += 1
                next5 = ugly_numbers[i5] * 5
                
        return ugly_numbers[-1]