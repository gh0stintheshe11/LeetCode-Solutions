class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for k, trim in queries:
            trimmed_nums = [(num[-trim:], i) for i, num in enumerate(nums)]
            trimmed_nums.sort()
            result.append(trimmed_nums[k-1][1])
        return result