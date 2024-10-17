COUNT = "count_count"
class Trie: 
    def __init__(self):
        self.root = {}
    def add_word(self, w) -> None:
        ans = 0
        r = self.root
        for idx, v in enumerate(w):
            prev_v = w[len(w) - 1 - idx]
            r = r.setdefault((v, prev_v), {})
            ans += r.get(COUNT, 0)
        r[COUNT] = r.get(COUNT, 0) + 1
        return ans

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        ans = 0
        for w in words:
            ans += trie.add_word(w)
        return ans