class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        targetIndices_set = set(targetIndices)
        
        pattern_indexes = defaultdict(list)
        for i, char in enumerate(pattern):
            pattern_indexes[char].append(i)
        for indexes in pattern_indexes.values():
            indexes.reverse()
        
        dp = {0: 0}  # number of removed indexes in prefix
        
        for i, char in enumerate(source):
            i_is_removed = int(i in targetIndices_set)
            for j in pattern_indexes[char]:
                prev = dp.get(j)
                if prev is None:
                    continue
                dp[j + 1] = min(
                    dp.get(j + 1, float('inf')),
                    prev + i_is_removed,
                )
        
        return len(targetIndices) - dp[len(pattern)]