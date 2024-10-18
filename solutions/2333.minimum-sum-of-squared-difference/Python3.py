from typing import List
from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_moves = k1 + k2
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        if total_moves == 0:
            return sum(d * d for d in diff)

        diff_count = Counter(diff)
        if 0 in diff_count:
            del diff_count[0]
        
        keys = sorted(diff_count.keys(), reverse=True)
        while total_moves > 0 and keys:
            max_diff = keys[0]
            count = diff_count[max_diff]
            next_diff = keys[1] if len(keys) > 1 else 0
            
            max_changes = min(total_moves, count * (max_diff - next_diff))
            moves_to_next = max_changes // count
            moves_leftover = max_changes % count

            diff_count[max_diff] -= count
            if diff_count[max_diff] == 0:
                del diff_count[max_diff]
                keys.pop(0)

            if max_diff - moves_to_next > 0:
                diff_count[max_diff - moves_to_next] = diff_count.get(max_diff - moves_to_next, 0) + count - moves_leftover
            if moves_leftover > 0:
                diff_count[max_diff - moves_to_next - 1] = diff_count.get(max_diff - moves_to_next - 1, 0) + moves_leftover

            total_moves -= max_changes
        
        return sum(d * d * freq for d, freq in diff_count.items())