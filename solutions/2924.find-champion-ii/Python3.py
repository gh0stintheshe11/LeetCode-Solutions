from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        
        for _, v in edges:
            in_degree[v] += 1
        
        champions = [i for i in range(n) if in_degree[i] == 0]
        
        if len(champions) == 1:
            return champions[0]
        else:
            return -1