class Solution:
    def differByOne(self, words: List[str]) -> bool:        
        for i in range(len(words[0])):
            mem = set()
            for word in words:    
                new_word = word[:i] + '*' + word[i+1:]
                if new_word in mem:
                    return True
                else:
                    mem.add(new_word)
                    
        return False