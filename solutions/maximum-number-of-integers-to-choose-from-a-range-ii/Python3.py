class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        hs = set()
        for e in banned:
            hs.add(e)
            
        lst = []
        for e in hs:
            lst.append(e)
        lst.sort()
        N = len(lst)

        prefix = [0]*N
        prefix[0] = lst[0]
        for i in range(1, N):
            prefix[i] = prefix[i-1] + lst[i]

        def check(mid):
            curSum = mid*(mid+1)/2
            if curSum > maxSum: return False

            smallerIdx = N
            for i in range(N-1, -1, -1):
                if lst[i] <= mid:
                    smallerIdx = i
                    break
            
            if smallerIdx == N: return True
            
            cnt = smallerIdx+1
            curSum -= prefix[smallerIdx]

            for i in range(mid+1, n+1):
                if i not in hs:
                    curSum += i
                    if curSum > maxSum: return False
                    cnt -= 1
                    if cnt == 0: break
            return cnt==0

        l = 0
        r = min(n, int(math.sqrt(2*maxSum)))

        ans = 0
        while l<=r:
            mid = (l+r)//2

            if check(mid):
                ans = max(ans, mid)
                l = mid+1
            else:
                r = mid-1
                
        return ans