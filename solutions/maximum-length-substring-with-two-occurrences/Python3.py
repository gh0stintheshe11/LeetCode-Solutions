class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        
        for start in range(n):
            char_count = {}
            end = start
            while end < n:
                char_count[s[end]] = char_count.get(s[end], 0) + 1

                if char_count[s[end]] > 2:  # invalid substring
                    break

                end += 1

            max_length = max(max_length, end - start)

        return max_length