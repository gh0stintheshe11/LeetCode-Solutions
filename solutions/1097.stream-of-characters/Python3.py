class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = []
        for word in words:
            node = self.trie
            for char in reversed(word):
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True
    
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for char in reversed(self.stream):
            if char in node:
                node = node[char]
                if '#' in node:
                    return True
            else:
                break
        return False