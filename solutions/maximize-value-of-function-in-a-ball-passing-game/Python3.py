class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        from math import log2, ceil
        n = len(receiver)
        max_steps = ceil(log2(k)) + 1
        
        last_receiver = [[0] * max_steps for _ in range(n)]
        sum_scores = [[0] * max_steps for _ in range(n)]
        
        for i in range(n):
            last_receiver[i][0] = receiver[i]
            sum_scores[i][0] = receiver[i]
        
        for j in range(1, max_steps):
            for i in range(n):
                prev_receiver = last_receiver[i][j - 1]
                last_receiver[i][j] = last_receiver[prev_receiver][j - 1]
                sum_scores[i][j] = sum_scores[i][j - 1] + sum_scores[prev_receiver][j - 1]
        
        max_score = 0
        
        for i in range(n):
            total_score = i
            current_pos = i
            remaining_k = k
            for j in range(max_steps - 1, -1, -1):
                if remaining_k >= (1 << j):
                    total_score += sum_scores[current_pos][j]
                    current_pos = last_receiver[current_pos][j]
                    remaining_k -= (1 << j)
            
            max_score = max(max_score, total_score)
        
        return max_score