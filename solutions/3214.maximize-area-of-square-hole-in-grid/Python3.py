class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        count_h = 1
        max_count_h = 0
        for i in range(1,len(hBars)):
            if hBars[i-1]+1==hBars[i]:
                count_h+=1 
            else:
                max_count_h= max(max_count_h,count_h)
                count_h = 1
        max_count_h= max(max_count_h,count_h)
        count_v= 1
        max_count_v = 0
        for i in range(1,len(vBars)):
            if vBars[i-1]+1==vBars[i]:
                count_v+=1 
            else:
                max_count_v= max(max_count_v,count_v)
                count_v = 1
        max_count_v= max(max_count_v,count_v)
        ans = min(max_count_h,max_count_v)+1
        return ans*ans