from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        count_1, count_2 = count[1], count[2]

        if count[0] % 2 == 0:
            return count_1 > 0 and count_2 > 0
        else:
            return abs(count_1 - count_2) > 2