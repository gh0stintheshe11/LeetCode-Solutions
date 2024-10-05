class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        current_weight = 0
        count = 0
        for w in weight:
            if current_weight + w <= 5000:
                current_weight += w
                count += 1
            else:
                break
        return count