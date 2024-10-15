class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canDivide(maxSize):
            operations = 0
            for num in nums:
                if num > maxSize:
                    # Calculate operations needed to make the bags not exceed maxSize
                    operations += (num - 1) // maxSize
            return operations <= maxOperations
        
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            if canDivide(mid):
                right = mid
            else:
                left = mid + 1
        
        return left