class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # Step 1: Finding the first decreasing element from the right side.
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                break
        else:
            return arr  # The array is already the smallest permutation.
        
        # Step 2: Find the largest element to the right of arr[i] that is smaller than arr[i].
        for j in range(n-1, i, -1):
            if arr[j] < arr[i] and arr[j] != arr[j-1]:
                arr[i], arr[j] = arr[j], arr[i]
                break
        
        return arr