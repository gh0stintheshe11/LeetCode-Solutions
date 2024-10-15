class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                res.append(words[i])
        return res