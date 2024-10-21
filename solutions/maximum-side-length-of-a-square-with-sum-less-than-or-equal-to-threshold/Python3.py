class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Create prefix sum matrix
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = mat[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

        def calculate_sum(x1, y1, x2, y2):
            return prefix_sum[x2 + 1][y2 + 1] - prefix_sum[x1][y2 + 1] - prefix_sum[x2 + 1][y1] + prefix_sum[x1][y1]

        left, right = 0, min(m, n)

        while left <= right:
            mid = (left + right) // 2
            found = False
            
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if calculate_sum(i, j, i + mid - 1, j + mid - 1) <= threshold:
                        found = True
                        break
                if found:
                    break

            if found:
                left = mid + 1
            else:
                right = mid - 1
                
        return right