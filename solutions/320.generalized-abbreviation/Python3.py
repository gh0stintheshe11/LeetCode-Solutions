class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def backtrack(pos, cur, count):
            if pos == len(word):
                res.append(cur + (str(count) if count > 0 else ''))
            else:
                # Abbreviate this character
                backtrack(pos + 1, cur, count + 1)
                # Keep this character
                backtrack(pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0)

        res = []
        backtrack(0, '', 0)
        return res