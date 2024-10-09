class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        arr1XorSum = 0
        arr2XorSum = 0
        
        for num in arr1:
            arr1XorSum ^= num
            
        for num in arr2:
            arr2XorSum ^= num
            
        return arr1XorSum & arr2XorSum