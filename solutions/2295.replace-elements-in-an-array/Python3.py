class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_to_index = {num: i for i, num in enumerate(nums)}
        
        for old_val, new_val in operations:
            index = num_to_index[old_val]
            nums[index] = new_val
            num_to_index[new_val] = index
            del num_to_index[old_val]
        
        return nums