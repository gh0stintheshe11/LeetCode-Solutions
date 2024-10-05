class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        start = 0
        l = len(s)
        
        for i in range(rows):
            start += cols
            if s[start % l] == ' ':
                start += 1
            else:
                while start > 0 and s[(start-1) % l] != ' ':
                    start -= 1
        
        return start // l