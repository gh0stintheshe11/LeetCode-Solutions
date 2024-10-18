
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        
        @cache
        def fn(val): 
            if val < x: return min(2*val-1, 2*(x-val))
            k = int(log(val)//log(x))
            ans = k + fn(val - x**k)
            if x**(k+1) < 2*val: 
                ans = min(ans, k + 1 + fn(x**(k+1) - val))
            return ans 
        
        return fn(target)
