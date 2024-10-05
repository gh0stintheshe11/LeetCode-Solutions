from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        
        def dfs(current):
            if current > n:
                return
            result.append(current)
            for i in range(10):
                next_num = current * 10 + i
                if next_num > n:
                    return
                dfs(next_num)
        
        for i in range(1, 10):
            dfs(i)
        
        return result