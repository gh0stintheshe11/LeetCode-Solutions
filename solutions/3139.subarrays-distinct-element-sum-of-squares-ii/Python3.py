class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        p=10**9+7
        dct={}
        for i, n in enumerate(nums):
            if n in dct:
                dct[n].append(i)
            else:
                dct[n]=[-1, i]
        curs={k:0 for k in dct.keys()}
        s2=0
        pw=1
        l=len(nums)
        while pw<l:
            pw<<=1
        
        tree=[0, pw, None, None, 0]
        def rec(t):
            if t[1]-t[0]>1:
                mid=(t[1]+t[0])>>1
                t[2]=[t[0], mid, None, None, 0]
                t[3]=[mid, t[1], None, None, 0]
                rec(t[2])
                rec(t[3])
        rec(tree)
        
        def up(t, a, b):
            if a==t[0] and b==t[1]:
                t[4]+=b-a
                return t[4]
            else:
                carry=(t[4]-t[2][4]-t[3][4])>>1
                t[2][4]+=carry
                t[3][4]+=carry
                mid=(t[1]+t[0])>>1
                tmp=0
                if a<mid:
                    tmp+=up(t[2], a, min(mid, b))
                if b>mid:
                    tmp+=up(t[3], max(mid, a), b)
                t[4]+=b-a
                return tmp
                    
        ans=0
        for n in nums:
            a=dct[n][curs[n]]+1
            curs[n]+=1
            b=dct[n][curs[n]]+1
            s2+=2*up(tree, a, b)-(b-a)
            s2%=p
            ans+=s2
        
        return ans%p