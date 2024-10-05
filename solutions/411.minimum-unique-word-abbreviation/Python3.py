from typing import List

class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        def get_abbr(word, mask):
            """Convert word to its abbreviation with the given mask."""
            abbr = []
            count = 0
            for i in range(len(word)):
                if mask & (1 << i):
                    if count != 0:
                        abbr.append(str(count))
                        count = 0
                    abbr.append(word[i])
                else:
                    count += 1
            if count != 0:
                abbr.append(str(count))
            return ''.join(abbr)

        def can_abbr(word, mask):
            """Check if word can be abbreviated with the given mask."""
            for i in range(len(word)):
                if mask & (1 << i) and target[i] != word[i]:
                    return False
            return True

        dictionary = [word for word in dictionary if len(word) == len(target)]
        if not dictionary:
            return str(len(target))
        
        n = len(target)
        masks = [i for i in range(1 << n)]
        valid_masks = set(range(1 << n))

        for word in dictionary:
            invalid_masks = set()
            for mask in masks:
                if can_abbr(word, mask):
                    invalid_masks.add(mask)
            valid_masks -= invalid_masks

        best_abbr = target
        for mask in valid_masks:
            abbr = get_abbr(target, mask)
            if len(abbr) < len(best_abbr):
                best_abbr = abbr

        return best_abbr