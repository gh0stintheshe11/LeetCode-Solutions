class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(start, n, path):
            if n == 1 and len(path) > 1:
                res.append(path[:])
                return
            for i in range(start, int(n ** 0.5) + 1):
                if n % i == 0:
                    path.append(i)
                    backtrack(i, n // i, path)
                    path.pop()
            if n >= start:
                path.append(n)
                backtrack(n, 1, path)
                path.pop()
        
        res = []
        backtrack(2, n, [])
        return res