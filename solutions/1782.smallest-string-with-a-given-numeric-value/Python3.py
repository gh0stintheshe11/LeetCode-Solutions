class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a'] * n
        k -= n
        
        i = n - 1
        while k > 0:
            increment = min(25, k)
            result[i] = chr(ord('a') + increment)
            k -= increment
            i -= 1
            
        return ''.join(result)