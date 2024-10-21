class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check if the characters at the even indices are the same in both strings,
        # and check if the characters at the odd indices are the same in both strings.
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])