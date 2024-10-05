class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros_to_duplicate = 0
        for num in arr:
            if num == 0:
                zeros_to_duplicate += 1
        
        # We will make a backward pass through the array
        # Start from the end
        i = n - 1
        j = n + zeros_to_duplicate - 1
        
        while i < j:
            if j < n:
                arr[j] = arr[i]
            
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            
            i -= 1
            j -= 1