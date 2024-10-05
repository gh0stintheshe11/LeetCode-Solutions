class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, count = float('-inf'), 0
        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                count += 1
        return count