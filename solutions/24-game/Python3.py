from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        import itertools
        
        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        for op in "+-*/":
                            if (op == "+" or op == "*") and i > j:
                                continue
                            if op == "/" and nums[j] == 0:
                                continue
                            
                            next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                            if op == "+":
                                next_nums.append(nums[i] + nums[j])
                            elif op == "-":
                                next_nums.append(nums[i] - nums[j])
                            elif op == "*":
                                next_nums.append(nums[i] * nums[j])
                            elif op == "/":
                                next_nums.append(nums[i] / nums[j])
                            
                            if helper(next_nums):
                                return True
            
            return False
        
        for perm in itertools.permutations(cards):
            if helper(list(perm)):
                return True
        
        return False