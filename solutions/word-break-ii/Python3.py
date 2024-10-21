class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            results = []
            if start == len(s):
                results.append("")

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    sublist = backtrack(end)
                    for sub in sublist:
                        results.append(word + ("" if sub == "" else " ") + sub)
            
            memo[start] = results
            return results

        wordSet = set(wordDict)
        memo = {}
        return backtrack(0)