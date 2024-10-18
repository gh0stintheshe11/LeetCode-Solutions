class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        max_score = 0
        zeros_count = 0
        ones_count = total_ones

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_count += 1
            else:
                ones_count -= 1
            
            max_score = max(max_score, zeros_count + ones_count)

        return max_score