class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 1:
            return 0
        m = len(strs[0])
        deletions = 0
        ordered = [False] * (n - 1)

        for col in range(m):
            if all(ordered[i] or strs[i][col] <= strs[i + 1][col] for i in range(n - 1)):
                for i in range(n - 1):
                    if strs[i][col] < strs[i + 1][col]:
                        ordered[i] = True
            else:
                deletions += 1

        return deletions