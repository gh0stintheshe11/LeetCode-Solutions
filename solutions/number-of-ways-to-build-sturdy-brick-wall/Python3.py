from typing import List
from itertools import combinations

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        MOD = 10**9 + 7

        def generate_rows(curr_width=0, used_combination=None):
            if used_combination is None:
                used_combination = []
            if curr_width == width:
                boundaries.add(tuple(used_combination))
            for b in bricks:
                if curr_width + b <= width:
                    generate_rows(curr_width + b, used_combination + [curr_width + b])

        def is_sturdy(row1, row2):
            return all(a not in row2 for a in row1[:-1])

        boundaries = set()
        generate_rows()

        n = len(boundaries)
        boundary_list = list(boundaries)
        sturdy_ways = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if is_sturdy(boundary_list[i], boundary_list[j]):
                    sturdy_ways[i][j] = 1

        dp = [1] * n
        for _ in range(1, height):
            new_dp = [0] * n
            for i in range(n):
                new_dp[i] = sum(dp[j] * sturdy_ways[j][i] for j in range(n)) % MOD
            dp = new_dp

        return sum(dp) % MOD