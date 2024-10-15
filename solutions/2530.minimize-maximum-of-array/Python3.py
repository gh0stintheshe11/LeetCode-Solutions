class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def isPossible(maxValue):
            carry = 0
            for num in nums:
                carry += num
                if carry > maxValue:
                    return False
                carry -= maxValue
            return True
        
        left, right = 0, max(nums)
        while left < right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left