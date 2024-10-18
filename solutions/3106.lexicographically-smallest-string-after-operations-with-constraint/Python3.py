class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans=""
        for st in s:
            if k<=0 or st=="a":
                ans+=st
                continue
            val=ord(st)-96     #making in  26 indexed 
            dis=0

            if val<=13:          # if before half
                dis=val-1
                if dis<=k: 
                    ans+="a"          # if possible making it a 
                else:                         
                    ans+= chr(ord(st)-k)     # else reducing it as much possible

            else:                        #second half
                dis=((26-val)+1)%26
                if dis<=k:
                    ans+="a"              # if possible making it a 
                else:
                    ans+= chr(ord(st)-k)     # else reducing it as much possible
            k-=dis
        return ans