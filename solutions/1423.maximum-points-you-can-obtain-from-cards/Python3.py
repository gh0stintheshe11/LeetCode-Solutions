class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_points = sum(cardPoints)
        min_subarray_sum = float('inf')
        current_sum = 0
        window_size = n - k

        if window_size == 0:
            return total_points

        for i in range(n):
            current_sum += cardPoints[i]
            if i >= window_size:
                current_sum -= cardPoints[i - window_size]
            if i >= window_size - 1:
                min_subarray_sum = min(min_subarray_sum, current_sum)

        return total_points - min_subarray_sum