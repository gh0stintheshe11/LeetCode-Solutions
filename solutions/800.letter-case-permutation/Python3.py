class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub="", i=0):
            if i == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].lower(), i + 1)
                    backtrack(sub + s[i].upper(), i + 1)
                else:
                    backtrack(sub + s[i], i + 1)

        res = []
        backtrack()
        return res