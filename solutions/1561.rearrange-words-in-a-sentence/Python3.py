class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        # Pair words with their original indices
        indexed_words = [(word, idx) for idx, word in enumerate(words)]
        # Sort by word length, then by original index
        indexed_words.sort(key=lambda x: (len(x[0]), x[1]))
        # Re-create the sentence with the sorted words
        sorted_sentence = [word for word, _ in indexed_words]
        # Lowercase the first word and capitalize the result
        sorted_sentence[0] = sorted_sentence[0].lower()
        result = ' '.join(sorted_sentence)
        return result.capitalize()