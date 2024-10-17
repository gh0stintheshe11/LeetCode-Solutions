class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:

        n = len(nums) 
        memo = [[] for _ in range(n)] 
        for i in range(n):
            for j in range(n):
                if i == j: continue
                memo[i].append((abs(i - nums[j]), j)) 

        bestPaths = {source: {} for source in range(n)}
        bestPaths[0][0] = (0, None) 
        masks = [2 ** i for i in range(n)] 
        def search(source: int, score: int, free: int) -> int:
            if free in bestPaths[source]:
                return score + bestPaths[source][free][0] 

            bestContinuation = 0xFF
            bestNextEl = None 
            for scoreDiff, nextEl in memo[source]:
                if free & masks[nextEl]: 
                    if not nextEl and free != 1: continue
                    nc = search(nextEl, score + scoreDiff, free ^ masks[nextEl]) 
                    if nc < bestContinuation or (nc == bestContinuation and nextEl < bestNextEl):
                        bestContinuation = nc 
                        bestNextEl = nextEl 
            bestPaths[source][free] = (bestContinuation - score, bestNextEl) 
            return bestContinuation 

        free = 2 ** n - 1 
        search(0, 0, free) 

        response = [0] 
        while (ne := bestPaths[response[-1]][free][1]) != 0: 
            response.append(ne) 
            free ^= masks[ne] 
        return response