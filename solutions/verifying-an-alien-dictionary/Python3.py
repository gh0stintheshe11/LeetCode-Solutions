class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: index for index, char in enumerate(order)}
        
        def compare(word1: str, word2: str) -> bool:
            min_length = min(len(word1), len(word2))
            for i in range(min_length):
                if word1[i] != word2[i]:
                    if order_map[word1[i]] > order_map[word2[i]]:
                        return False
                    return True
            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return False
        return True