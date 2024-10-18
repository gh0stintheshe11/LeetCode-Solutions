class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        halfLength = (intLength + 1) // 2
        start = 10**(halfLength - 1)
        result = []
        
        for q in queries:
            halfPalindrome = start + q - 1
            halfStr = str(halfPalindrome)
            if len(halfStr) > halfLength:
                result.append(-1)
            else:
                if intLength % 2 == 0:
                    fullPalindrome = halfStr + halfStr[::-1]
                else:
                    fullPalindrome = halfStr + halfStr[-2::-1]
                result.append(int(fullPalindrome))
                
        return result