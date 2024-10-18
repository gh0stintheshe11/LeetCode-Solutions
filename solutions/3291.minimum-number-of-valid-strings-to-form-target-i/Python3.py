class TrieNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else {}
        
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        wordsTrie = TrieNode(0) # null node
        
        for word in words:
            wordsTrie = self.addToTrie(wordsTrie, word)
        
        n = len(target)
        t = [-1]*(n+1)
        
        def rec(i, target, wordsTrie):
            if t[i] != -1:
                return t[i]
            if i >= len(target):
                return 0
            else:
                covered_prefix_len = self.get_match_len(wordsTrie, target[i:])
                if covered_prefix_len == 0:
                    return float('inf')
                else:
                    next_candidates = [rec(j+1, target, wordsTrie) for j in range(i, i+covered_prefix_len)]
                    t[i] = 1 + min(next_candidates)
                    return t[i]
        
        out = rec(0, target, wordsTrie)
        if out == float('inf'):
            out = -1
        
        return out
    
    def addToTrie(self, currTrie, word):
        n = len(word)
        nodeHead = currTrie
        for i in range(n):
            curr_char = word[i]
            if curr_char not in currTrie.children:
                currTrie.children[curr_char] = TrieNode(curr_char)
                
            currTrie = currTrie.children[curr_char]
        
        return nodeHead
    
    def get_match_len(self, currTrieNode, target):
        l = 0
        for ch in target:
            if ch not in currTrieNode.children:
                break
            currTrieNode = currTrieNode.children[ch]
            l += 1
        return l