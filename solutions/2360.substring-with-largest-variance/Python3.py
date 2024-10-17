from collections import defaultdict
import itertools

class Solution:
    def largestVariance(self, s: str) -> int:
        char_count = defaultdict(int)
        char_index = defaultdict(list)
        for i, ch in enumerate(s):
            char_count[ch] += 1
            char_index[ch].append((i, ch))

        max_variance = 0
        for char_a, char_b in itertools.permutations(char_count.keys(), 2):
            total, has_b = 0, False
            if char_count[char_b] - 1 > max_variance:
                for _, x in sorted(char_index[char_a] + char_index[char_b]):
                    if x == char_a and (has_b := total > 0):
                        total -= 1
                    elif x == char_b:
                        max_variance = max(max_variance, total + has_b)
                        total += 1
        return max_variance