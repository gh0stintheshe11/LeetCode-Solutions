from typing import List

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = set(dictionary)
        self.abbr_map = {}
        
        for word in self.dictionary:
            abbr = self._get_abbr(word)
            if abbr not in self.abbr_map:
                self.abbr_map[abbr] = word
            else:
                if self.abbr_map[abbr] != word:
                    self.abbr_map[abbr] = ""

    def isUnique(self, word: str) -> bool:
        abbr = self._get_abbr(word)
        if abbr not in self.abbr_map:
            return True
        if self.abbr_map[abbr] == word:
            return True
        return False

    def _get_abbr(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)