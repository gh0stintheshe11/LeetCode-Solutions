class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(x):
            return x == x[::-1]
        
        L, R = int(left), int(right)
        count = 0

        for i in range(1, 100000):
            s = str(i)
            palindromes = [int(s + s[-2::-1]), int(s + s[::-1])]
            for pal in palindromes:
                pal_square = pal * pal
                if pal_square > R:
                    break
                if pal_square >= L and is_palindrome(str(pal_square)):
                    count += 1

        return count