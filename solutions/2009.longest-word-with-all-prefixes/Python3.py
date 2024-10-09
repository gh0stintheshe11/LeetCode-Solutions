class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        words.sort(key=lambda x: (-len(x), x))
        
        for word in words:
            if all(word[:i] in word_set for i in range(1, len(word) + 1)):
                return word
        
        return ""