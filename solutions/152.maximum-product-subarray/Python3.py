class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')
        cur_max, cur_min = 1, 1

        for num in nums:
            if num == 0:
                cur_max, cur_min = 1, 1
                max_product = max(max_product, 0)
                continue
            
            tmp = cur_max * num
            cur_max = max(num, tmp, cur_min * num)
            cur_min = min(num, tmp, cur_min * num)
            max_product = max(max_product, cur_max)
        
        return max_product