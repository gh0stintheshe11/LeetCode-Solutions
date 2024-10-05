class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
            
        target_sum = total_sum // 3
        current_sum, count = 0, 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum == target_sum:
                count += 1
                current_sum = 0
            if count == 2 and i < len(arr) - 1:
                return True
        
        return False