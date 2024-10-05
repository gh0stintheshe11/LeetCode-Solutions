from typing import List

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        nearest = {
            1: [-1] * n,
            2: [-1] * n,
            3: [-1] * n
        }
        
        # Forward pass
        last_seen = {-1: -1, 1: -1, 2: -1, 3: -1}
        for i in range(n):
            color = colors[i]
            last_seen[color] = i
            for c in range(1, 4):
                if last_seen[c] != -1:
                    nearest[c][i] = i - last_seen[c]

        # Backward pass
        last_seen = {-1: -1, 1: -1, 2: -1, 3: -1}
        for i in range(n-1, -1, -1):
            color = colors[i]
            last_seen[color] = i
            for c in range(1, 4):
                if last_seen[c] != -1:
                    dist = last_seen[c] - i
                    if nearest[c][i] == -1 or nearest[c][i] > dist:
                        nearest[c][i] = dist

        # Answer queries
        result = []
        for index, color in queries:
            result.append(nearest[color][index])

        return result