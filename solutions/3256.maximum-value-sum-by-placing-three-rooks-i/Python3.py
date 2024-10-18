from typing import List
import itertools

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])

        # Store the largest 3 values for each row with their column indices
        row_max = []
        for row in board:
            largest_three = sorted([(v, j) for j, v in enumerate(row)], reverse=True)[:3]
            row_max.append(largest_three)

        max_sum = float('-inf')

        # Iterate over each combination of 3 different rows
        for r1, r2, r3 in itertools.combinations(range(m), 3):
            # For a fixed choice of 3 rows, try all combinations of non-attacking column choices
            for col1_choice in row_max[r1]:
                v1, col1 = col1_choice
                for col2_choice in row_max[r2]:
                    v2, col2 = col2_choice
                    if col2 == col1:
                        continue
                    for col3_choice in row_max[r3]:
                        v3, col3 = col3_choice
                        if col3 == col1 or col3 == col2:
                            continue
                        max_sum = max(max_sum, v1 + v2 + v3)

        return max_sum