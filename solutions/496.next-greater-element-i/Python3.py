class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        
        # Traverse nums2 and fill the next_greater dictionary
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # For all elements left in the stack, there is no next greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Prepare the result for nums1 using the next_greater dictionary
        return [next_greater[num] for num in nums1]