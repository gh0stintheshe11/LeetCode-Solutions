class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Convert lists to sets to ignore duplicates within each list
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        
        # Initialize a set to store the results
        result_set = set()
        
        # Look for numbers present in at least two out of the three sets
        result_set.update(set1 & set2)
        result_set.update(set1 & set3)
        result_set.update(set2 & set3)
        
        # Convert the set to a list to return the result
        return list(result_set)