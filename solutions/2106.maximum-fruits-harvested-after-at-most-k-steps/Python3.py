class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        return self.max_fruits_sliding_window(fruits, startPos, k)
    
    def max_fruits_sliding_window(self, fruits, start_pos, k):
        max_fruits, f = 0, 0
        start = 0
        for end, [p, a] in enumerate(fruits):
            f += a
            if p < start:
                continue

            while start <= end and p - fruits[start][0] + min(abs(start_pos - p), abs(start_pos - fruits[start][0])) > k:
                f -= fruits[start][1]
                start += 1

            max_fruits = max(max_fruits, f)

        return max_fruits