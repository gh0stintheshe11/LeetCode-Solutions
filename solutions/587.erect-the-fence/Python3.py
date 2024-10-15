from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        # Sort the points lexicographically (tuples compare lexicographically, which is what we want).
        points = sorted(map(tuple, trees))
        
        if len(points) < 4:
            return points
        
        # Build the lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)
        
        # Build the upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)
        
        # Remove the last point of each half because it's repeated at the beginning of the other half
        return list(set(lower[:-1] + upper[:-1]))