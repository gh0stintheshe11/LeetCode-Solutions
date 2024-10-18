class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        ans = 0
        cnt = prev = -1 
        for i, x in enumerate(word): 
            curr = vowels.index(x)
            if cnt >= 0: # in the middle of counting 
                if 0 <= curr - prev <= 1: 
                    cnt += 1
                    if x == "u": ans = max(ans, cnt)
                elif x == "a": cnt = 1
                else: cnt = -1 
            elif x == "a": cnt = 1
            prev = curr 
        return ans