class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        hens.sort()
        grains = list(sorted(set(grains)))
        m, n = len(hens), len(grains)
        
        def check(mid):
            j = 0
            for i in range(len(hens)):
                left_dist = 0
                if j < n and grains[j] < hens[i]:
                    if hens[i] - grains[j] > mid: return False
                    left_dist += hens[i] - grains[j]
                    j += 1
                    while j < n and grains[j] <= hens[i]:
                        j += 1
                while j < n and 2*left_dist + grains[j] - hens[i] <= mid:
                    j += 1
                while j < n and grains[j] > hens[i] and 2*(grains[j] - hens[i]) + left_dist <= mid:
                    j += 1
            return j == n
        
        left, right = 0, 2 * max(max(grains), max(hens))
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
                
        return left