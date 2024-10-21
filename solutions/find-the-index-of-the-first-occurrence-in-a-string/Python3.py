class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use the built-in find method to locate the first occurrence of needle in haystack
        return haystack.find(needle)