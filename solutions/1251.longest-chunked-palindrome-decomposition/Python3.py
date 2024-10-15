class Solution:
    def longestDecomposition(self, text: str) -> int:
        def longestDecompositionHelper(s: str) -> int:
            n = len(s)
            if n == 0:
                return 0
            for i in range(n // 2):
                if s[:i + 1] == s[n - i - 1:]:
                    return 2 + longestDecompositionHelper(s[i + 1:n - i - 1])
            return 1

        return longestDecompositionHelper(text)