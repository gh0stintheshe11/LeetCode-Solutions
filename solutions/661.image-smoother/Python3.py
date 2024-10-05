from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                count, total = 0, 0
                for i in range(max(r-1, 0), min(r+2, m)):
                    for j in range(max(c-1, 0), min(c+2, n)):
                        total += img[i][j]
                        count += 1
                result[r][c] = total // count
        
        return result