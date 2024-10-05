from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_key(s):
            key = []
            # Calculate the relative difference between each character:
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                key.append(diff)
            return tuple(key)
        
        groups = defaultdict(list)
        for string in strings:
            key = get_key(string)
            groups[key].append(string)
        
        return list(groups.values())