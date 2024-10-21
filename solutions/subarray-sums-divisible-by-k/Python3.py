from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_sum_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder < 0:
                remainder += k
            if remainder in prefix_sum_count:
                count += prefix_sum_count[remainder]
                prefix_sum_count[remainder] += 1
            else:
                prefix_sum_count[remainder] = 1
                
        return count