from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        a_len = len(a)
        b_len = len(b)

        # Find all positions where substring a starts
        a_indices = [i for i in range(n - a_len + 1) if s[i:i + a_len] == a]

        # Find all positions where substring b starts
        b_indices = [j for j in range(n - b_len + 1) if s[j:j + b_len] == b]

        # Find beautiful indices
        beautiful_indices = []
        b_index_pos = 0

        for i in a_indices:
            # Move b_index_pos to the first j where b_indices[j] >= i - k
            while b_index_pos < len(b_indices) and b_indices[b_index_pos] < i - k:
                b_index_pos += 1

            # Check if current b_index_pos satisfies the condition |b_indices[b_index_pos] - i| <= k
            if b_index_pos < len(b_indices) and b_indices[b_index_pos] <= i + k:
                beautiful_indices.append(i)

        return beautiful_indices