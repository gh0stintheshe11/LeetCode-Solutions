class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda k: (k[0], -k[1]))   # left to right, up to down
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                cx, cy = points[i]
                tx, ty = points[j]
                if cy < ty: continue   # C below T, not feasible
                between = False
                for k in range(i + 1, j):
                    kx, ky = points[k]
                    if cx <= kx <= tx and cy >= ky >= ty:
                        between = True
                        break
                if not between: 
                    result += 1
        return result