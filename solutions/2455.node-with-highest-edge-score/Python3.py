from typing import List

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        
        for i, node in enumerate(edges):
            scores[node] += i
        
        max_score = -1
        max_index = -1
        
        for i, score in enumerate(scores):
            if score > max_score or (score == max_score and i < max_index):
                max_score = score
                max_index = i
        
        return max_index