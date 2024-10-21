class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        from collections import defaultdict

        class TrieNode:
            def __init__(self):
                self.children = {}
                self.score = 0

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, word):
                current = self.root
                for char in word:
                    if char not in current.children:
                        current.children[char] = TrieNode()
                    current = current.children[char]
                    current.score += 1

            def get_prefix_score(self, word):
                current = self.root
                total_score = 0
                for char in word:
                    if char in current.children:
                        current = current.children[char]
                        total_score += current.score
                return total_score

        trie = Trie()

        for word in words:
            trie.insert(word)

        return [trie.get_prefix_score(word) for word in words]