class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            if strs[i][::-1] > strs[i]:
                strs[i] = strs[i][::-1]
        
        best = ""
        for i in range(len(strs)):
            s = strs[i]
            for k in (s, s[::-1]):
                for j in range(len(k)):
                    candidate = k[j:] + "".join(strs[i+1:]) + "".join(strs[:i]) + k[:j]
                    if candidate > best:
                        best = candidate
        return best