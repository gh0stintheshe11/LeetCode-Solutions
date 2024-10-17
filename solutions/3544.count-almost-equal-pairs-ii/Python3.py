from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        available_set = []

        visited = defaultdict(lambda: 0)

        for ele in nums:
            ele = str(ele)
            if len(ele) < 7:
                ele = '0' * (7 - len(ele)) + ele
            available_set.append(ele)
            
        count = 0
        for ele in available_set:
            generated_set = set()
            count += visited[ele]
            generated_set.add(ele)
            ele = list(ele)
            for i in range(7):
                for ii in range(i + 1, 7):
                    ele[i], ele[ii] = ele[ii], ele[i]
                    digit = "".join(ele)
                    if digit not in generated_set:
                        generated_set.add(digit)
                        count += visited[digit]
                    for iii in range(7):
                        for iv in range(iii + 1, 7):
                            ele[iii], ele[iv] = ele[iv], ele[iii]
                            digit = "".join(ele)
                            if digit not in generated_set:
                                count += visited[digit]
                                generated_set.add(digit)
                            ele[iii], ele[iv] = ele[iv], ele[iii]
                    ele[i], ele[ii] = ele[ii], ele[i]
            digit = "".join(ele)
            visited[digit] += 1
        
        return count