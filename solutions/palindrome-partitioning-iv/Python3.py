class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        # Create a table to store the palindrome status of substrings
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Fill the table
        for length in range(1, n + 1):  # length of substring
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 1:
                    is_palindrome[start][end] = True
                elif length == 2:
                    is_palindrome[start][end] = (s[start] == s[end])
                else:
                    is_palindrome[start][end] = (s[start] == s[end] and is_palindrome[start + 1][end - 1])
        
        # Try to find three non-empty palindromic substrings
        for i in range(1, n - 1):
            for j in range(i, n):
                if is_palindrome[0][i - 1] and is_palindrome[i][j - 1] and is_palindrome[j][n - 1]:
                    return True
        
        return False