from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        trim_count = n // 20
        trimmed_arr = arr[trim_count:n - trim_count]
        return sum(trimmed_arr) / len(trimmed_arr)