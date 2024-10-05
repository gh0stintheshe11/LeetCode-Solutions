from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string to form the key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list corresponding to the sorted key
            anagrams[sorted_str].append(s)
        
        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())