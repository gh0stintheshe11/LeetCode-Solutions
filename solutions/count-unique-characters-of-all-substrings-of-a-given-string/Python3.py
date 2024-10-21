class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {c: [-1, -1] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        res = 0
        for i, char in enumerate(s):
            k, j = index[char]
            res += (i - j) * (j - k)
            index[char] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(s) - j) * (j - k)
        return res