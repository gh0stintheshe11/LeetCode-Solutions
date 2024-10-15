class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def create_palindrome(s: str):
            left_part = s[:(len(s) + 1) // 2]
            if len(s) % 2 == 0:
                return left_part + left_part[::-1]
            else:
                return left_part + left_part[-2::-1]
        
        def adjust_and_create_palindrome(s: str, adjustment: int):
            left_part = s[:(len(s) + 1) // 2]
            left_part = str(int(left_part) + adjustment)
            return create_palindrome(left_part + s[(len(s) + 1) // 2:])
        
        # Edge case
        if n == "1":
            return "0"
        
        num = int(n)
        candidates = set()
        
        # Original palindrome
        palindrome = create_palindrome(n)
        if palindrome != n:
            candidates.add(int(palindrome))
        
        # Edge cases where length changes
        candidates.add(10 ** len(n) + 1)
        candidates.add(10 ** (len(n) - 1) - 1)
        
        # Create palindromes by adjusting the prefix
        candidates.add(int(adjust_and_create_palindrome(n, 1)))
        candidates.add(int(adjust_and_create_palindrome(n, -1)))
        
        # Remove the original number
        candidates.discard(num)
        
        # Find the closest palindrome
        closest, min_diff = None, float('inf')
        for candidate in candidates:
            diff = abs(candidate - num)
            if diff < min_diff or (diff == min_diff and candidate < closest):
                min_diff = diff
                closest = candidate

        return str(closest)