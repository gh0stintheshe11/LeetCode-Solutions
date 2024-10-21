class Solution:
    def maximumBooks(self, A: List[int]) -> int:
        n = len(A)

        res = 0
        st = []
        ss = 0
        for i in range(n):
            while st and A[st[-1]] + (i-st[-1]) >= A[i]:
                j = st.pop()
                l = j - st[-1] if st else min(j+1, A[j])
                s = (A[j]+A[j]-l+1) * l //2
                ss -= s

            l = i - st[-1] if st else min(i+1, A[i])
            s = (A[i]+A[i]-l+1) * l //2
            ss += s
            st.append(i)
            res = max(res, ss)
        return res