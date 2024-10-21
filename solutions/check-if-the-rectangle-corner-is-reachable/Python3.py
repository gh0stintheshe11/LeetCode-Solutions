def countercw(a,b,c):
    x,y = (b[0]-a[0], b[1]-a[1]), (c[0]-b[0], c[1]-b[1])
    return x[0]*y[1] - x[1]*y[0] >= 0

def touch(ra, rb):
    return (ra[0]-rb[0])**2 + (ra[1]-rb[1])**2 <= (ra[2]+rb[2])**2

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        uf = list(range(n+2))
        
        def find(x):
            if uf[x]!=x: uf[x] = find(uf[x])
            return uf[x]
        
        def union(x,y):
            x,y = find(x), find(y)
            if x<y: x,y = y,x
            uf[y] = x
        
        ignores = [False]*n
        for i,c in enumerate(circles):
            x,y,r = c
            if touch(c, (xCorner, yCorner, 0)): return False
            elif x>xCorner and y>yCorner: ignores[i]=True
            elif x>xCorner:
                if x>xCorner+r: ignores[i]=True
                else: union(i, n)
            elif y>yCorner:
                if y>yCorner+r: ignores[i]=True
                else: union(i,n+1)
            else:
                if y<=r or xCorner-x <= r: union(i,n)
                if x<=r or yCorner-y <= r: union(i,n+1)
        
        for i in range(n):
            if ignores[i]: continue
            for j in range(i+1, n):
                if ignores[j]: continue
                a,b = circles[i], circles[j]
                if not touch(a,b): continue
                if a[0]<b[0]: a,b = b,a
                if (a[0]<=xCorner and a[1]<=yCorner) or (b[0]<=xCorner and b[1]<=yCorner): union(i,j)
                elif countercw((a[0], a[1]), (xCorner, yCorner), (b[0], b[1])): union(i,j)
        
        return find(n)!=find(n+1)