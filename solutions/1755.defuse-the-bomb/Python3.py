class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        if k == 0:
            return [0] * n
        
        result = [0] * n
        if k > 0:
            for i in range(n):
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
        else:
            k = -k
            for i in range(n):
                result[i] = sum(code[(i - j) % n] for j in range(1, k + 1))
        
        return result