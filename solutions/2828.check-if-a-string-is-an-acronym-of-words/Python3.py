class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(word[0] for word in words) == s