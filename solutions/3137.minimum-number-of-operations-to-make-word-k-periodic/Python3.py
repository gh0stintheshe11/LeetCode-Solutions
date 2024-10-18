from collections import defaultdict

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        kDict = defaultdict(int)
        for i in range(0, len(word), k):
            kDict[word[i : i + k]] += 1
        
        return sum(kDict.values()) - max(kDict.values())