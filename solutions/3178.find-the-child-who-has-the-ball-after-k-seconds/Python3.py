class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        period = 2 * (n - 1)
        k = k % period
        direction = 1
        position = 0

        for _ in range(k):
            position += direction
            if position == 0 or position == n - 1:
                direction *= -1
        
        return position