from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Combine the words from both sentences
        combined_words = words1 + words2
        
        # Count the occurrences of each word
        word_count = Counter(combined_words)
        
        # Find the words that appear exactly once
        uncommon_words = [word for word in word_count if word_count[word] == 1]
        
        return uncommon_words
