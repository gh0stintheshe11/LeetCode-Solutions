class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        merged_dict = defaultdict(int)
        
        for id_val in nums1 + nums2:
            id, val = id_val
            merged_dict[id] += val
        
        return sorted([[id, val] for id, val in merged_dict.items()])