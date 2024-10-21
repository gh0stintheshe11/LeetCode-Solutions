class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        
        largest_from_left = [(nums[0], 0)]
        smallest_from_right = [(nums[-1], len(nums) - 1)]

        for idx, val in enumerate(nums):
            if val > largest_from_left[-1][0]:
                largest_from_left.append((val, idx))

        for idx in range(len(nums))[::-1]:
            val = nums[idx]
            if val < smallest_from_right[-1][0]:
                smallest_from_right.append((val, idx))
        
        smallest_from_right = smallest_from_right[::-1]
        largest_idx = 0 
        smallest_idx = 0
        best_len = 0
        while largest_idx < len(largest_from_left) and smallest_idx < len(smallest_from_right):
            l_val, l_idx = largest_from_left[largest_idx]
            s_val, s_idx = smallest_from_right[smallest_idx]

            if l_val > s_val:
                best_len = max(best_len, s_idx - l_idx + 1)
                smallest_idx += 1
            else:
                largest_idx += 1
        
        return best_len