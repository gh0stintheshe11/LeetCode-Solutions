class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        if n == 0:
            return []
        
        max_from_right = -1
        
        for i in range(n - 1, -1, -1):
            new_value = max_from_right
            if arr[i] > max_from_right:
                max_from_right = arr[i]
            arr[i] = new_value
        
        return arr