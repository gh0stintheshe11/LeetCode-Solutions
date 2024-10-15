from typing import List

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        
        def max_left_peaks():
            left_peaks = [0] * n
            stack = []
            for i in range(n):
                while stack and maxHeights[stack[-1]] > maxHeights[i]:
                    stack.pop()
                if stack:
                    prev_index = stack[-1]
                    left_peaks[i] = left_peaks[prev_index] + maxHeights[i] * (i - prev_index)
                else:
                    left_peaks[i] = maxHeights[i] * (i + 1)
                stack.append(i)
            return left_peaks
        
        def max_right_peaks():
            right_peaks = [0] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and maxHeights[stack[-1]] > maxHeights[i]:
                    stack.pop()
                if stack:
                    next_index = stack[-1]
                    right_peaks[i] = right_peaks[next_index] + maxHeights[i] * (next_index - i)
                else:
                    right_peaks[i] = maxHeights[i] * (n - i)
                stack.append(i)
            return right_peaks
        
        left_sums = max_left_peaks()
        right_sums = max_right_peaks()
        
        max_sum = 0
        for i in range(n):
            max_sum = max(max_sum, left_sums[i] + right_sums[i] - maxHeights[i])
        
        return max_sum