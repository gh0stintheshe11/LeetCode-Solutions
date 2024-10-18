class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        
        char_map = defaultdict(list)
        for index, char in enumerate(s):
            char_map[char].append(index)
        
        def is_subsequence(word):
            prev_index = -1
            for char in word:
                if char not in char_map:
                    return False
                # Binary search for the smallest index greater than prev_index
                lo, hi = 0, len(char_map[char])
                while lo < hi:
                    mid = (lo + hi) // 2
                    if char_map[char][mid] > prev_index:
                        hi = mid
                    else:
                        lo = mid + 1
                if lo == len(char_map[char]):
                    return False
                prev_index = char_map[char][lo]
            return True
        
        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1
        return count