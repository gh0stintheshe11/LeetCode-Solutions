class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        pattern_0, pattern_1 = pattern
        if pattern_0 == pattern_1:
            return self.mSCsame(text, pattern)
        else:
            pattern_0_indices = []
            pattern_1_indices = []
            for i, c in enumerate(text):
                if c == pattern_0:
                    pattern_0_indices.append(i)
                elif c == pattern_1:
                    pattern_1_indices.append(i)
            n_patterns_added = max(len(pattern_1_indices), len(pattern_0_indices))

            n_patterns_initially = 0
            for pattern_0_index in pattern_0_indices:
                index_index = bisect.bisect(pattern_1_indices, pattern_0_index)
                if index_index < len(pattern_1_indices):
                    n_patterns_initially += len(pattern_1_indices) - index_index
            return n_patterns_initially + n_patterns_added

    def mSCsame(self, text, pattern):
        n_pattern_0 = text.count(pattern[0]) + 1
        return n_pattern_0 * (n_pattern_0 - 1) // 2