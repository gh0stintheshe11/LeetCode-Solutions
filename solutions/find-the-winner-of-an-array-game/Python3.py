class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        max_val = arr[0]
        win_count = 0

        if k >= len(arr):
            return max(arr)
        
        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
                win_count = 1
            else:
                win_count += 1

            if win_count == k:
                return max_val
            
        return max_val