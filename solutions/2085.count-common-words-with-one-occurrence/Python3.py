class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        return sum(1 for word in count1 if count1[word] == 1 and count2.get(word, 0) == 1)