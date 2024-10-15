class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_word = False

        def build_trie(words):
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_word = True
            return root

        def dfs(board, node, i, j, path, res):
            if node.is_word:
                res.add(path)
                node.is_word = False  # avoid duplicate words

            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                char = board[i][j]
                if char in node.children:
                    board[i][j] = '#'  # mark visited
                    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        dfs(board, node.children[char], i + x, j + y, path + char, res)
                    board[i][j] = char  # unmark visited

        trie = build_trie(words)
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, trie, i, j, "", res)
                
        return list(res)