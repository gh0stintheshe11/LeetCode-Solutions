class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_count = 0  # Number of times this is end of a word
        self.prefix_count = 0  # Number of words with this prefix

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.prefix_count += 1
        current.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        current = self.root
        for char in word:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.word_count

    def countWordsStartingWith(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.prefix_count

    def erase(self, word: str) -> None:
        current = self.root
        nodes = [current]
        for char in word:
            current = current.children[char]
            nodes.append(current)
        
        current.word_count -= 1
        
        for i in range(len(word)):
            nodes[i + 1].prefix_count -= 1
            if nodes[i + 1].prefix_count == 0:
                del nodes[i].children[word[i]]
                break