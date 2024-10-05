from collections import defaultdict
from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        on_lamps = set()
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        diag_count = defaultdict(int)
        anti_diag_count = defaultdict(int)
        
        # Initialize lamp states
        for r, c in lamps:
            if (r, c) not in on_lamps:
                on_lamps.add((r, c))
                row_count[r] += 1
                col_count[c] += 1
                diag_count[r - c] += 1
                anti_diag_count[r + c] += 1
        
        result = []
        
        # Answer each query and turn off the appropriate lamps
        for qr, qc in queries:
            if row_count[qr] > 0 or col_count[qc] > 0 or diag_count[qr - qc] > 0 or anti_diag_count[qr + qc] > 0:
                result.append(1)
            else:
                result.append(0)
            
            for dr, dc in directions:
                nr, nc = qr + dr, qc + dc
                if (nr, nc) in on_lamps:
                    on_lamps.remove((nr, nc))
                    row_count[nr] -= 1
                    col_count[nc] -= 1
                    diag_count[nr - nc] -= 1
                    anti_diag_count[nr + nc] -= 1
        
        return result