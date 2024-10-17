class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.extend([[1, 0], [n, n-1]])
        restrictions.sort()
        
        for i in reversed(range(len(restrictions)-1)): 
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])
        
        ans = 0 
        for i in range(1, len(restrictions)): 
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0])
            ans = max(ans, (restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0] + restrictions[i][1])//2)
        return ans