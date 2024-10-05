from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4
        
        for i in range(n):
            if i + threshold < n and arr[i] == arr[i + threshold]:
                return arr[i]

        return arr[0]