class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        div = [0] * n
        current_number = 0
        
        for i, char in enumerate(word):
            current_number = (current_number * 10 + int(char)) % m
            if current_number == 0:
                div[i] = 1
            else:
                div[i] = 0
                
        return div