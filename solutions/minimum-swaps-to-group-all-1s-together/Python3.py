class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones_count = sum(data)
        if ones_count == 0:
            return 0
        
        max_ones_in_window = 0
        curr_ones_in_window = 0
        left = 0
        
        for right in range(len(data)):
            curr_ones_in_window += data[right]
            
            if right - left + 1 > ones_count:
                curr_ones_in_window -= data[left]
                left += 1
            
            if right - left + 1 == ones_count:
                max_ones_in_window = max(max_ones_in_window, curr_ones_in_window)
        
        return ones_count - max_ones_in_window