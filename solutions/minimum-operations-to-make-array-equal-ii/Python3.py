class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        
        sum_inc = 0
        sum_dec = 0

        for num1, num2 in zip(nums1, nums2):
            diff = num2 - num1
            
            if diff % k != 0:
                return -1
            
            if diff > 0:
                sum_inc += diff // k
            elif diff < 0:
                sum_dec += (-diff) // k

        return sum_inc if sum_inc == sum_dec else -1