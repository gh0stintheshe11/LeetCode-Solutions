class Solution:
    def countDistinct(self, s: str) -> int:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_end = False

        root = TrieNode()
        distinct_count = 0

        for i in range(len(s)):
            node = root
            for j in range(i, len(s)):
                char = s[j]
                if char not in node.children:
                    node.children[char] = TrieNode()
                    distinct_count += 1
                node = node.children[char]

        return distinct_count