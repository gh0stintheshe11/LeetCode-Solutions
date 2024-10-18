from collections import defaultdict
from typing import List

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mapping_dict = defaultdict(set)
        for old, new in mappings:
            mapping_dict[old].add(new)

        l_s, l_sub = len(s), len(sub)
        
        for start in range(l_s - l_sub + 1):
            found = True
            for i in range(l_sub):
                if s[start + i] != sub[i] and s[start + i] not in mapping_dict[sub[i]]:
                    found = False
                    break
            if found:
                return True
                
        return False