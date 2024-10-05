class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1
            
        return True