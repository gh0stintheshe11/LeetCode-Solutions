class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        n = len(nums)

        smallest_elem_idx = 0
        largest_elem_idx = n-1
        
        for i in range(n):
            if nums[i] < nums[smallest_elem_idx]:
                smallest_elem_idx = i
        
        for i in range(n-1, -1, -1):
            if nums[i] > nums[largest_elem_idx]:
                largest_elem_idx = i
        
        total_swaps = 0

        total_swaps += (smallest_elem_idx - 0)
        total_swaps += (n-1 - largest_elem_idx)

        if smallest_elem_idx > largest_elem_idx:
            total_swaps -= 1
        
        return total_swaps