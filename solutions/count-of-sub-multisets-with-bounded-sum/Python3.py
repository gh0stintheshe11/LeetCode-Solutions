class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        s=sum(nums)
        if l>s:
            return 0
        r=min(r, s)
        d=defaultdict(int)
        for n in nums:
            d[n]+=1
        lst=list(d.items())
        lst.sort(key=lambda x:-x[0])
        mult=1
        if lst[-1][0]==0:
            mult+=lst.pop()[1]
        p=10**9+7
        dct=[0]*(r+1)
        dct[0]=1
        for k, (n, m) in enumerate(lst):
            for cur in range(r-n+1):
                dct[cur+n]+=dct[cur]
            m=n*(m+1)
            for cur in range(r, m-1, -1):
                dct[cur]-=dct[cur-m]
            if k%20==0:
                for val in range(r+1):
                    dct[val]%=p
        return sum(dct[val] for val in range(l, r+1))*mult%p