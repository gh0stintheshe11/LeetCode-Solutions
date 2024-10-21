class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def check(a, b):
            i, j = 0, len(a) - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            return is_palindrome(a, i, j) or is_palindrome(b, i, j)
        
        return check(a, b) or check(b, a)