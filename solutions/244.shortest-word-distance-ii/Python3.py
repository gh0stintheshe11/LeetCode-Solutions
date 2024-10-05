from typing import List

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indices = {}
        for index, word in enumerate(wordsDict):
            if word not in self.word_indices:
                self.word_indices[word] = []
            self.word_indices[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        i, j = 0, 0
        min_dist = float('inf')
        
        while i < len(indices1) and j < len(indices2):
            min_dist = min(min_dist, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1
        
        return min_dist