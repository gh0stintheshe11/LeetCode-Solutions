class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(n):
            s = str(n)
            if len(s) % 2 != 0:
                return False
            n = len(s) // 2
            return sum(int(s[i]) for i in range(n)) == sum(int(s[i]) for i in range(n, len(s)))
        
        count = 0
        for num in range(low, high + 1):
            if is_symmetric(num):
                count += 1
        
        return count