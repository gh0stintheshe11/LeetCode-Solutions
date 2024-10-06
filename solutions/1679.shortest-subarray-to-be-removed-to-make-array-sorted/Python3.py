class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        # Find the non-decreasing subarray from the start
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
            
        # If the entire array is non-decreasing, return 0
        if left == n - 1:
            return 0
        
        # Find the non-decreasing subarray from the end
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Initial result could be removing one of the ends
        min_to_remove = min(n - left - 1, right)
        
        # Try to find the best overlap between left and right
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                min_to_remove = min(min_to_remove, j - i - 1)
                i += 1
            else:
                j += 1
        
        return min_to_remove