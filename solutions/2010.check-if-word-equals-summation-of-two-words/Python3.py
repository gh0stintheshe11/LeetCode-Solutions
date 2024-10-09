class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def word_to_number(word: str) -> int:
            return int(''.join(str(ord(char) - ord('a')) for char in word))
        
        first_value = word_to_number(firstWord)
        second_value = word_to_number(secondWord)
        target_value = word_to_number(targetWord)
        
        return first_value + second_value == target_value