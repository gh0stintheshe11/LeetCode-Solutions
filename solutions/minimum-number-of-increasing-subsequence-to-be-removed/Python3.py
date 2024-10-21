class Solution:
    def minOperations(self, A):
        A, lis = A[::-1], []
        for v in A:
            index = bisect_right(lis, v)
            if index >= len(lis): lis.append(v)
            else: lis[index] = v
        return len(lis)