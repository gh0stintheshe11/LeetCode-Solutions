class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        ones = 0
        
        for char in s:
            if char == '1':
                ones += 1
                count = (count + ones) % MOD
            else:
                ones = 0
        
        return count