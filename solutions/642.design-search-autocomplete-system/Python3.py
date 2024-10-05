from collections import defaultdict
import heapq

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences_count = defaultdict(int)
        self.current_sentence = ''
        for sentence, time in zip(sentences, times):
            self.sentences_count[sentence] += time

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.sentences_count[self.current_sentence] += 1
            self.current_sentence = ''
            return []
        
        self.current_sentence += c
        candidates = [(count, sentence) for sentence, count in self.sentences_count.items() if sentence.startswith(self.current_sentence)]
        candidates.sort(key=lambda x: (-x[0], x[1]))
        return [sentence for count, sentence in candidates[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)