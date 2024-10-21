class Trie:
    def __init__(self):
        self.word = None
        self.children = {}
    def insert(self, word):
        current = self
        size = len(word)
        for i in range(size-1, -1, -1):
            if word[i] not in current.children:
                current.children[word[i]] = Trie()
            current = current.children[word[i]]
        current.word = word

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        idx = 0
        idxMap = {}
        m = math.inf
        for i in range(len(original)):
            if original[i] not in idxMap:
                idxMap[original[i]] = idx
                idx += 1
            if changed[i] not in idxMap:
                idxMap[changed[i]] = idx
                idx += 1
        w = [[m]*idx for _ in range(idx)]

        for i in range(len(original)):
            w[idxMap[changed[i]]][idxMap[changed[i]]] = 0
            w[idxMap[original[i]]][idxMap[original[i]]] = 0
            w[idxMap[original[i]]][idxMap[changed[i]]] = min(w[idxMap[original[i]]][idxMap[changed[i]]], cost[i])

        for k in range(idx):
            for i in range(idx):
                if i != k:    
                    for j in range(idx):
                        if i != j and j != k and w[i][k] != m and w[k][j] != m: 
                            w[i][j] = min(w[i][j], w[i][k] + w[k][j])

        dp = [m] * (len(source) + 1)
        dp[0] = 0

        sourceRoot = Trie()
        targetRoot = Trie()
        
        for i in range(len(original)):
            sourceRoot.insert(original[i])
            targetRoot.insert(changed[i])

        for i in range(1, len(source) + 1):
            if source[i - 1] == target[i - 1]:
                dp[i] = dp[i-1]
            
            s = sourceRoot
            t = targetRoot

            for j in range(i-1, -1, -1):
                if source[j] not in s.children or target[j] not in t.children:
                    break
                t = t.children[target[j]]
                s = s.children[source[j]]
                if dp[j] != m and s.word != None and t.word != None:
                    dp[i] = min(dp[i], dp[j] + w[idxMap[s.word]][idxMap[t.word]])
        
        return dp[-1] if dp[-1] < m else -1