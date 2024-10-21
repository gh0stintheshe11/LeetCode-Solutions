class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        power = list(set(power))
        power.sort()
        n = len(power)
        
        @cache
        def recur(ind):
            if ind >= n: return 0
            
            notTake = recur(ind + 1)
            take = float('-inf')
            
            pos = bisect_left(power, power[ind] + 2 + 1)
            take = (cnt[power[ind]] * power[ind]) + recur(pos)
            
            return max(take, notTake)
    
        return recur(0)