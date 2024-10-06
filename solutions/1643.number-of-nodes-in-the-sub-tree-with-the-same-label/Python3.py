from collections import defaultdict, Counter
from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        result = [0] * n
        
        def dfs(node, parent):
            counter = Counter()
            label = labels[node]
            counter[label] += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                sub_counter = dfs(neighbor, node)
                counter.update(sub_counter)
            
            result[node] = counter[label]
            return counter
        
        dfs(0, -1)
        return result