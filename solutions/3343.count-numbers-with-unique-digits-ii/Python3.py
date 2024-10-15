class Solution:
    def numberCount(self, a: int, b: int) -> int:
        def hasUniqueDigits(num):
            num_str = str(num)
            return len(num_str) == len(set(num_str))
        
        count = 0
        for num in range(a, b + 1):
            if hasUniqueDigits(num):
                count += 1
        
        return count