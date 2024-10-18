class Solution:
    def maximumLength(self, s: str) -> int:
        max_len = -1
        n = len(s)
        
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                substring = s[start:start + length]
                if len(set(substring)) == 1:
                    count = sum(
                        1 for i in range(n - length + 1) if s[i:i + length] == substring
                    )
                    if count >= 3:
                        max_len = len(substring)
        
        return max_len