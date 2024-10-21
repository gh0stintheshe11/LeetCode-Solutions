class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        
        total_chars = Counter()
        
        for word in words:
            total_chars.update(word)
        
        n = len(words)
        for count in total_chars.values():
            if count % n != 0:
                return False
        
        return True