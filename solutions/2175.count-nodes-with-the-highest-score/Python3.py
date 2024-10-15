from typing import List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        
        for node in range(1, n):
            children[parents[node]].append(node)
        
        def dfs(node):
            nonlocal max_score, max_count
            total_nodes = 1
            score = 1
            for child in children[node]:
                child_size = dfs(child)
                total_nodes += child_size
                score *= child_size
            
            if node != 0:
                score *= (n - total_nodes)
                
            if score > max_score:
                max_score = score
                max_count = 1
            elif score == max_score:
                max_count += 1
            
            return total_nodes
        
        max_score = 0
        max_count = 0
        dfs(0)
        return max_count