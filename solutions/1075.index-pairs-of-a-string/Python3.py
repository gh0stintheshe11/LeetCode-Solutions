class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        result = []
        for word in words:
            start = text.find(word)
            while start != -1:
                result.append([start, start + len(word) - 1])
                start = text.find(word, start + 1)
        result.sort()
        return result