class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(path):
            if len(path) == n:
                res.append(path)
                return
            for ch in 'abc':
                if not path or path[-1] != ch:
                    backtrack(path + ch)

        res = []
        backtrack("")
        return res[k - 1] if k <= len(res) else ""