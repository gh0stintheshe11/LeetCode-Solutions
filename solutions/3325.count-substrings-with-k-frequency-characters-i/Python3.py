class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        substrings = 0
        counts = [0]*26

        start = 0
        for i in range(len(s)):
            counts[ord(s[i])-ord('a')] += 1
            for j in range(len(counts)):
                if counts[j]>=k:
                    after = len(s)-i
                    while counts[j]>=k:
                        counts[ord(s[start])-ord('a')] -= 1
                        substrings += after
                        start += 1
        
        return substrings