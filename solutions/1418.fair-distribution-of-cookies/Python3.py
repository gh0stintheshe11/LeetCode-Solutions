from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        n = len(cookies)
        
        def backtrack(index, max_unfairness):
            if index == n:
                return max_unfairness
            result = float('inf')
            for i in range(k):
                children[i] += cookies[index]
                result = min(result, backtrack(index + 1, max(max_unfairness, children[i])))
                children[i] -= cookies[index]
                if children[i] == 0:  # Optimization: avoid wasting time
                    break
            return result
        
        return backtrack(0, 0)