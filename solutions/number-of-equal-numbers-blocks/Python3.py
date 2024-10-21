# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass

class Solution(object):
    def countBlocks(self, nums: 'BigArray') -> int:
        length = nums.size()
        if length == 0:
            return 0
        
        count = 0
        i = 0
        
        while i < length:
            count += 1
            current_value = nums.at(i)
            
            # Find the end of the current block using binary search
            low, high = i, length - 1
            while low < high:
                mid = (low + high + 1) // 2
                if nums.at(mid) == current_value:
                    low = mid
                else:
                    high = mid - 1
            i = low + 1
        
        return count