class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        vertical_words = []

        for i in range(max_length):
            vertical_word = []
            for word in words:
                if i < len(word):
                    vertical_word.append(word[i])
                else:
                    vertical_word.append(' ')
            vertical_words.append(''.join(vertical_word).rstrip())

        return vertical_words