class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
        words = sentence.split()
        
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in root_set:
                    return word[:i]
            return word
        
        return ' '.join(replace(word) for word in words)