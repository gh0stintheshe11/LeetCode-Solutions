class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        l, r, n  = 0, 0, len(word)
        z = [0] * n
        for i in range(k, n, k):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and word[z[i]] == word[i + z[i]]:
                z[i] += 1
            if z[i] == n - i:
                return i // k
            if i + z[i] >= r:
                r = i + z[i] - 1
                l = i
        return ceil(len(word)/k)