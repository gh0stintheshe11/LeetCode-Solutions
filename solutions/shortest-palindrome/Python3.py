class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Create a new string which is s + '#' + reverse(s)
        rev_s = s[::-1]
        new_s = s + '#' + rev_s
        
        # Compute the KMP table for the new string
        n = len(new_s)
        lps = [0] * n  # Longest Prefix Suffix table
        
        # Build the LPS table
        j = 0  # length of previous longest prefix suffix
        for i in range(1, n):
            while (j > 0 and new_s[i] != new_s[j]):
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
                lps[i] = j
        
        # The length of the longest palindromic prefix
        longest_palindromic_prefix_length = lps[-1]
        
        # Characters to be added in front of s to make it a palindrome
        to_add = rev_s[:len(s) - longest_palindromic_prefix_length]
        
        return to_add + s
