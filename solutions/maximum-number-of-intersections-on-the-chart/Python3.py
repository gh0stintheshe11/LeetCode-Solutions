class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        axis, res, cur, edge = defaultdict(int), 0, 0, 0
        for x in range(1, len(y) - 1):
            if y[x - 1] < y[x] > y[x + 1]:      
                axis[y[x]] -= 2
            elif y[x - 1] > y[x] < y[x + 1]:    
                axis[y[x]] += 2

        axis[y[0]] += 1 if y[0] < y[1] else -1
        axis[y[-1]] += 1 if y[-1] < y[-2] else -1
        if y[0] == y[-1]:
            if (y[0] < y[1]) ^ (y[-1] < y[-2]):
                edge = 1
            elif y[0] < y[1] and not axis[y[0]]:
                edge = 2
        
        for line in sorted(axis):
            if line == y[0]:
                if edge == 1:
                    cur += (axis[line] >> 1) + 1
                    if res < cur:   
                        res = cur
                    cur += (axis[line] >> 1) - 1
                    continue
                elif edge == 2:
                    if res < cur + 1:   
                        res = cur + 1
                    continue
            cur += axis[line]
            if res < cur:   
                res = cur
            
        return res