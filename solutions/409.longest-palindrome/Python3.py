class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        count = Counter(s)
        length = 0
        odd_found = False

        for char_count in count.values():
            if char_count % 2 == 0:
                length += char_count
            else:
                length += char_count - 1
                odd_found = True

        if odd_found:
            length += 1

        return length