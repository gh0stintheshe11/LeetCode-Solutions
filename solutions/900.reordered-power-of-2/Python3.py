class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter

        def countDigits(n):
            return Counter(str(n))

        target = countDigits(n)
        
        for i in range(31):  # 2^30 is slightly over 10^9
            if countDigits(1 << i) == target:
                return True
        
        return False