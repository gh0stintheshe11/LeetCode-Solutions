from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Reverse the arrays to make addition easier (from least significant to most significant bit)
        arr1.reverse()
        arr2.reverse()
        
        # Placeholders for the length of the arrays
        n1, n2 = len(arr1), len(arr2)
        
        # Length of the result can be max(n1, n2) + 2 to accommodate all possible carries
        max_len = max(n1, n2) + 2
        result = [0] * max_len
        
        carry = 0
        
        # Addition in negabinary
        for i in range(max_len):
            value = carry
            if i < n1:
                value += arr1[i]
            if i < n2:
                value += arr2[i]
            
            result[i] = value & 1  # The current bit of result
            carry = -(value >> 1)  # Get the next carry, considering negabinary properties
        
        # Reverse result and remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        result.reverse()
        return result