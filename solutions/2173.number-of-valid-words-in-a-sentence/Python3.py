class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid_word(word):
            if any(ch.isdigit() for ch in word):
                return False
            
            hyphen_count = 0
            for i, ch in enumerate(word):
                if ch == '-':
                    hyphen_count += 1
                    if hyphen_count > 1:
                        return False
                    # Hyphen must be surrounded by letters
                    if i == 0 or i == len(word) - 1 or not (word[i - 1].isalpha() and word[i + 1].isalpha()):
                        return False
                elif ch in "!.,":  # punctuation check
                    if i != len(word) - 1:
                        return False
            
            return True

        tokens = sentence.split()
        return sum(is_valid_word(token) for token in tokens)