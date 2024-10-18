class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [float('inf')] * n

        # First pass: left to right
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev

        # Second pass: right to left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            answer[i] = min(answer[i], prev - i)
        
        return answer