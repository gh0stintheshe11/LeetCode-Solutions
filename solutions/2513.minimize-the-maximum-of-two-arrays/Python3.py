class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def dfs(x):
            return x-x//divisor1 >= uniqueCnt1 and x-x//divisor2 >= uniqueCnt2 and x-x//math.lcm(divisor1,divisor2) >= uniqueCnt1 + uniqueCnt2

        low, high = 1, 10**10 

        while low <= high:
            mid = (low+high)//2 

            if dfs(mid):
                high = mid-1 
            else:
                low = mid+1 

        return low