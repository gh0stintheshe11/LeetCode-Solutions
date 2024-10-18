from typing import List
from bisect import bisect_right

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        total_package_size = sum(packages)
        min_wasted_space = float('inf')
        MOD = 10**9 + 7

        for box_sizes in boxes:
            box_sizes.sort()
            if box_sizes[-1] < packages[-1]:
                continue

            current_waste = 0
            previous_index = 0

            for box in box_sizes:
                index = bisect_right(packages, box)
                current_waste += box * (index - previous_index)
                previous_index = index

            min_wasted_space = min(min_wasted_space, current_waste)

        if min_wasted_space == float('inf'):
            return -1

        return (min_wasted_space - total_package_size) % MOD