from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Pre-calculate prefix sum of plates
        prefix_plates = [0] * n
        for i in range(n):
            if s[i] == '*':
                prefix_plates[i] = (prefix_plates[i - 1] + 1) if i > 0 else 1
            else:
                prefix_plates[i] = prefix_plates[i - 1] if i > 0 else 0
        
        # Pre-calculate the nearest candle to the left and right
        left_candle = [-1] * n
        right_candle = [-1] * n
        current_left_candle = -1
        current_right_candle = -1
        
        for i in range(n):
            if s[i] == '|':
                current_left_candle = i
            left_candle[i] = current_left_candle
        
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                current_right_candle = i
            right_candle[i] = current_right_candle
        
        result = []
        # Process each query
        for left, right in queries:
            # Find the nearest candles within the bounds
            l_candle = right_candle[left]
            r_candle = left_candle[right]
            
            if l_candle == -1 or r_candle == -1 or l_candle >= r_candle:
                result.append(0)
            else:
                result.append(prefix_plates[r_candle] - prefix_plates[l_candle])
        
        return result