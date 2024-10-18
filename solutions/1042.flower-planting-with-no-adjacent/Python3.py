class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        # Initialize adjacency list
        adj = defaultdict(list)
        for x, y in paths:
            adj[x].append(y)
            adj[y].append(x)
        
        # Initialize the answer array with 0 (no flower assigned yet)
        answer = [0] * n
        
        for garden in range(1, n + 1):
            # Find the flowers used by adjacent gardens
            used_flowers = {answer[neighbor - 1] for neighbor in adj[garden]}
            
            # Assign the first available flower type
            for flower_type in range(1, 5):
                if flower_type not in used_flowers:
                    answer[garden - 1] = flower_type
                    break
        
        return answer