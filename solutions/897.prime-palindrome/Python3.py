class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        def next_palindrome(x):
            s = str(x)
            half = s[:(len(s) + 1) // 2]
            next_pal = int(half + half[::-1][len(s) % 2:])
            if next_pal >= x:
                return next_pal
            half = str(int(half) + 1)
            return int(half + half[::-1][len(s) % 2:])
        
        if n <= 2:
            return 2
        if n == 3:
            return 3
        candidate = n
        if candidate % 2 == 0:
            candidate += 1
        
        while True:
            candidate = next_palindrome(candidate)
            if is_prime(candidate):
                return candidate
            candidate += 2