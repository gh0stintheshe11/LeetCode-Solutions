from typing import List

class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n < 3:
            return arr
        
        while True:
            new_arr = arr[:]
            for i in range(1, n - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new_arr[i] += 1
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new_arr[i] -= 1
            
            if new_arr == arr:
                break
            
            arr = new_arr
        
        return arr