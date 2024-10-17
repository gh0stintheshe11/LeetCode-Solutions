class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        l=[]
        n=len(s)
        for i in range(n):
            l+=[s[i]]
        i=n-1
        while i>=0 and l[i]==chr(97+k-1):
            l[i]="a"
            i-=1
        else:
            if i==-1:
                return ""
            l[i]=chr(ord(l[i])+1)
        i=0
        p=-1
        for i in range(n):
            if i+1<n:
                if l[i]==l[i+1]:
                    p=i+1
                    break
                if i+2<n:
                    if l[i]==l[i+2]:
                        p=i+2
                        break
        if p==-1:
            s1=""
            for i in l:
                s1+=i
            return s1
        a=self.solve(l,p,k)
        if a==-1:
            return ""
        l1=["a","b","c"]
        s1=""
        for i in range(n):
            if i<a:
                s1+=l[i]
            else:
                for j in range(3):
                    if i-2>=0:
                        if l1[j]!=l[i-1] and l1[j]!=l[i-2]:
                            l[i]=l1[j]
                            s1+=l[i]
                            break
                    elif i-1>=0:
                        if l1[j]!=l[i-1]:
                            l[i]=l1[j]
                            s1+=l[i]
                            break
                    else:
                        l[i]=l1[j]
                        s1+=l[i]
                        break
        return s1
    def solve(self,l,p,k):
        f=1
        while p>0:
            if p-1>=0:
                if l[p]==l[p-1]==chr(97+k-1):
                    if (p-2)<0:
                        return -1
                    l[p-2]=chr(ord(l[p-2])+1)
                    l[p-1]="a"
                    l[p]="b"
                    f=p
                    continue
                elif l[p-1]==l[p]:
                    l[p]=chr(ord(l[p])+1)
                    f=p
                    continue
            if p-2>=0:
                if l[p-2]==l[p]==chr(97+k-1):
                    l[p-1]=chr(ord(l[p-1])+1)
                    l[p]="a"
                    f=p
                    continue
                elif l[p-2]==l[p]:
                    l[p]=chr(ord(l[p])+1)
                    f=p
                    continue
            p-=1
        return f+1