class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        MOD = 10**9 + 7
        count = 0
        
        end = -1
        for start, finish in ranges:
            if start > end:
                count += 1
                end = finish
            else:
                end = max(end, finish)
        
        # For each separate non-overlapping group found, we have 2 choices (group 1 or group 2)
        return pow(2, count, MOD)