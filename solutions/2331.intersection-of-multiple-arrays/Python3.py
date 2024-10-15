class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []
        
        # Start with the set of the first list
        common_elements = set(nums[0])
        
        # Intersect with every other set
        for array in nums[1:]:
            common_elements.intersection_update(array)
            
        return sorted(common_elements)