class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similarity_map = {}
        
        for x, y in similarPairs:
            if x not in similarity_map:
                similarity_map[x] = set()
            if y not in similarity_map:
                similarity_map[y] = set()
            similarity_map[x].add(y)
            similarity_map[y].add(x)
        
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and (word2 not in similarity_map.get(word1, set())):
                return False
        
        return True