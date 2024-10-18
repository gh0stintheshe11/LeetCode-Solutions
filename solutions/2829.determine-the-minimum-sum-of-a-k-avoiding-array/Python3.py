class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        used = set()
        sum_val = 0
        current_num = 1
        
        while len(used) < n:
            if k - current_num not in used:
                used.add(current_num)
                sum_val += current_num
            current_num += 1
        
        return sum_val