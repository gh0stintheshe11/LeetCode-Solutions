from typing import List
from collections import defaultdict

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def get_abbreviation(word, prefix_len):
            if len(word) - prefix_len <= 3:
                return word
            return word[:prefix_len + 1] + str(len(word) - 2 - prefix_len) + word[-1]
        
        n = len(words)
        result = [get_abbreviation(word, 0) for word in words]
        prefix_len = [0] * n
        while True:
            to_update = defaultdict(list)
            for idx, abbr in enumerate(result):
                to_update[abbr].append(idx)
            
            no_conflicts = True
            for same_abbr_indexes in to_update.values():
                if len(same_abbr_indexes) > 1:
                    no_conflicts = False
                    for idx in same_abbr_indexes:
                        prefix_len[idx] += 1
                        result[idx] = get_abbreviation(words[idx], prefix_len[idx])
            
            if no_conflicts:
                break
        
        return result