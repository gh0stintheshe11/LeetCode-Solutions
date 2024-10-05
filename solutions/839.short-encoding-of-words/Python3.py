class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        for word in list(words):
            for k in range(1, len(word)):
                words.discard(word[k:])
        return sum(len(word) + 1 for word in words)