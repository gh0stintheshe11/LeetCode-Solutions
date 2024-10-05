class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_distance = float('inf')
        index1 = index2 = -1
        same_word = (word1 == word2)

        for i, word in enumerate(wordsDict):
            if word == word1:
                if same_word:
                    if index1 != -1:
                        min_distance = min(min_distance, i - index1)
                    index1 = i
                else:
                    index1 = i
                    if index2 != -1:
                        min_distance = min(min_distance, abs(index1 - index2))
            elif word == word2:
                index2 = i
                if index1 != -1:
                    min_distance = min(min_distance, abs(index1 - index2))
                    
        return min_distance