class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        d = {}
        pre = 0
        s = list(s)
        for i in range(len(s)):
            pre += int(s[i])

            if pre not in d:
                d[pre] = [i,i]
            else:
                if i > d[pre][1] :
                    d[pre][1] = i

        res = []
        
        for i in d:
            if i == k:
                res.append(int("".join(s[0:d[i][0]+1])))
            if i - k in d:
                res.append(int("".join(s[d[i-k][1]+ 1 : d[i][0]+1])))
        
        if len(res) == 0:
            return ""
        else:
            return str(min(res))