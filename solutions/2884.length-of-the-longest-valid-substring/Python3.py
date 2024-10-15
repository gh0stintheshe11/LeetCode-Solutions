class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        max_len = 0
        left = 0
        right = 0
        n = len(word)

        while right < n:
            is_valid = True
            for length in range(1, 11):
                if right - length + 1 < left:
                    break
                if word[right - length + 1:right + 1] in forbidden_set:
                    left = right - length + 2
                    is_valid = False
                    break
            if is_valid:
                max_len = max(max_len, right - left + 1)
            right += 1

        return max_len