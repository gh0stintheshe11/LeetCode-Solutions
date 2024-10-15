class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_set = set()

        for char in word:
            if 'a' <= char <= 'z':
                lower_set.add(char)
            elif 'A' <= char <= 'Z':
                upper_set.add(char)

        special_count = 0
        for char in lower_set:
            if char.upper() in upper_set:
                special_count += 1

        return special_count