class Solution:
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:
        merged_start = []
        merged_end = []
        for left, right in sorted(intervals):
            if merged_start and left <= merged_end[-1]:
                merged_end[-1] = max(merged_end[-1], right)
            else:
                merged_start.append(left)
                merged_end.append(right)
        ans = 0 
        for i, end in enumerate(merged_end):
            ans = max(ans, bisect_left(merged_start, end + k + 1) - i - 1)
        return len(merged_start) - ans