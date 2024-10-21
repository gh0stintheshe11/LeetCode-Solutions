class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Ensure words1 is the shorter one
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        
        left = 0
        while left < len(words1) and words1[left] == words2[left]:
            left += 1
        
        right = 0
        while right < len(words1) - left and words1[len(words1) - 1 - right] == words2[len(words2) - 1 - right]:
            right += 1

        return left + right == len(words1)