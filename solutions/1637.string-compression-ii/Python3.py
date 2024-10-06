class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from functools import lru_cache
        
        # Function to calculate length of RLE compression
        def rle_length(x: int) -> int:
            return 1 if x == 1 else 1 + len(str(x))
        
        @lru_cache(None)
        def dp(i: int, k: int) -> int:
            if k < 0:
                return float('inf')
            if i == len(s):
                return 0
            
            # Try to delete the current character
            res = dp(i + 1, k - 1)
            
            length = 0  # length of the sequence
            same_count = 0  # number of same characters
            j = i
            while j < len(s) and (k - same_count) >= 0:
                if s[j] == s[i]:
                    length += 1
                else:
                    same_count += 1
                if (k - same_count) >= 0:
                    res = min(res, dp(j + 1, k - same_count) + rle_length(length))
                j += 1
            
            return res
        
        return dp(0, k)