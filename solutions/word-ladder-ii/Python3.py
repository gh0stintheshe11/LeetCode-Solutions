from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordList = set(wordList)
        level = {beginWord}
        parents = defaultdict(list)
        
        while level and endWord not in parents:
            next_level = defaultdict(list)
            for word in level:
                for i in range(len(word)):
                    prefix, suffix = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            next_word = prefix + c + suffix
                            if next_word in wordList and next_word not in parents:
                                next_level[next_word].append(word)
            level = next_level
            parents.update(next_level)
        
        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append([beginWord] + path[::-1])
                return
            for parent in parents[word]:
                backtrack(parent, path + [word])
        
        if endWord in parents:
            backtrack(endWord, [])
        
        return res