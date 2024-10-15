class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            new_chars = ''.join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in word)
            word += new_chars
        return word[k - 1]