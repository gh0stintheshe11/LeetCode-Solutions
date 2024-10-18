class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        ans = [[0] * n for _ in range(m)]
        s = collections.deque()                   # a deque behave like mono-stack
        for i in range(m):                        # look right
            for j in range(n-1, -1, -1):
                num = heights[i][j]
                idx = bisect.bisect_left(s, num)  # binary search on an increasing order sequence
                ans[i][j] += idx + (idx < len(s)) # if `idx` is not out of bound, meaning the next element in `s` is the first one large than `num`, we can count it too
                while s and s[0] <= num:          # keep a mono-descreasing stack
                    s.popleft()
                s.appendleft(num)    
            s.clear()
        for j in range(n):                        # look below
            for i in range(m-1, -1, -1):
                num = heights[i][j]
                idx = bisect.bisect_left(s, num)
                ans[i][j] += idx + (idx < len(s))
                while s and s[0] <= num:
                    s.popleft()
                s.appendleft(num)    
            s.clear()
        return ans