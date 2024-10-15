from typing import List

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        seen_rows = set()
        seen_cols = set()
        total = 0

        for t, idx, val in reversed(queries):
            if t == 0:  # Row operation
                if idx not in seen_rows:
                    total += val * (n - len(seen_cols))
                    seen_rows.add(idx)
            else:  # Column operation
                if idx not in seen_cols:
                    total += val * (n - len(seen_rows))
                    seen_cols.add(idx)
        
        return total