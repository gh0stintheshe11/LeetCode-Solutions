from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        sum_grid = [[0] * n for _ in range(m)]
        count_grid = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                valid = True
                current_values = [image[i+k][j+l] for k in range(3) for l in range(3)]

                for k in range(3):
                    for l in range(3):
                        if k < 2:
                            if abs(image[i+k][j+l] - image[i+k+1][j+l]) > threshold:
                                valid = False
                        if l < 2:
                            if abs(image[i+k][j+l] - image[i+k][j+l+1]) > threshold:
                                valid = False
                
                if valid:
                    avg_intensity = sum(current_values) // 9

                    for k in range(3):
                        for l in range(3):
                            sum_grid[i+k][j+l] += avg_intensity
                            count_grid[i+k][j+l] += 1

        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if count_grid[i][j] > 0:
                    result[i][j] = sum_grid[i][j] // count_grid[i][j]
                else:
                    result[i][j] = image[i][j]

        return result