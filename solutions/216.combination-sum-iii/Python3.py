class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, remaining_k, remaining_n, path):
            if remaining_k == 0 and remaining_n == 0:
                result.append(path)
                return
            if remaining_k == 0 or remaining_n < 0:
                return
            
            for i in range(start, 10):
                backtrack(i + 1, remaining_k - 1, remaining_n - i, path + [i])
        
        result = []
        backtrack(1, k, n, [])
        return result