class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        sum_original = 0
        sum_sorted = 0
        chunks = 0
        
        for a, s in zip(arr, sorted_arr):
            sum_original += a
            sum_sorted += s
            if sum_original == sum_sorted:
                chunks += 1
                
        return chunks