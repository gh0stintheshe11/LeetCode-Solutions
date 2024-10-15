from collections import Counter
from typing import List

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        answer = []
        
        while len(sums) > 1:
            delta = sums[1] - sums[0]
            subset_with_delta = []
            subset_without_delta = []
            counter_sums = Counter(sums)
            
            for x in sums:
                if counter_sums[x] == 0:
                    continue
                subset_with_delta.append(x)
                subset_without_delta.append(x + delta)
                
                counter_sums[x] -= 1
                counter_sums[x + delta] -= 1

            subset_with_delta.sort()
            subset_without_delta.sort()

            if 0 in subset_with_delta:
                answer.append(delta)
                sums = subset_with_delta
            else:
                answer.append(-delta)
                sums = subset_without_delta
        
        return answer