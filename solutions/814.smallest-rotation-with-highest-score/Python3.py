class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [0] * (n + 1)
        
        for i in range(n):
            low = (i + 1) % n
            high = (i - nums[i] + n + 1) % n
            change[low] += 1
            change[high] -= 1
            if low >= high:
                change[0] += 1
        
        bestK = 0
        maxScore = -1
        score = 0
        
        for k in range(n):
            score += change[k]
            if score > maxScore:
                maxScore = score
                bestK = k
        
        return bestK