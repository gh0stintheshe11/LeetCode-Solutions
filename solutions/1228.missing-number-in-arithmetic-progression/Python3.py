class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = (n + 1) * (arr[0] + arr[-1]) // 2
        actual_sum = sum(arr)
        return total_sum - actual_sum