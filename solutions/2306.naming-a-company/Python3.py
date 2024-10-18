class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        nameMap = collections.defaultdict(set)
        result = 0

        for word in ideas: 
            nameMap[word[0]].add(word[1:])
            
        keys = list(nameMap.keys())
        n = len(keys)
        
        for char1 in range(n):
    
            for char2 in range(char1 + 1, n):
                key1, key2 = keys[char1], keys[char2]
                
                value1, value2 = nameMap[key1], nameMap[key2]
      
                duplicated_suffixes = len(value1 & value2)
                
                if key1 == key2: continue
                
                result += (len(value1) - duplicated_suffixes) * (len(value2) - duplicated_suffixes) * 2

        return result