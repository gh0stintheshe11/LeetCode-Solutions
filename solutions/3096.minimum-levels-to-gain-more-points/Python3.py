class Solution:
    def minimumLevels(self, A: List[int]) -> int:
        N = len(A)
        if not sum(A):
            return -1 if N <= 2 else 1
        A = [1 if x == 1 else -1 for x in A]
        L, R = A[:], A[:]
        for i in range(1, N):
            j = N - 1 - i
            L[i] += L[i - 1]
            R[j] += R[j + 1]
        return min([i + 1 for i in range(N - 1) if L[i] > R[i + 1]] or [-1])