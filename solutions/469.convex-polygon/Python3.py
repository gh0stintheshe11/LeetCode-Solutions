class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def cross_product(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        
        n = len(points)
        prev = 0
        
        for i in range(n):
            curr = cross_product(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if curr != 0:
                if curr * prev < 0:
                    return False
                prev = curr
        
        return True