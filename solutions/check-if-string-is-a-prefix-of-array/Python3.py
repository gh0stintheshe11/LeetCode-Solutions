from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concatenated = ""
        for word in words:
            concatenated += word
            if concatenated == s:
                return True
            if len(concatenated) > len(s):
                return False
        return False