class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter
        
        count = Counter(num)
        half_palindrome = []
        middle_char = ''
        
        for digit in map(str, range(9, -1, -1)):
            if count[digit] >= 2:
                pairs = count[digit] // 2
                half_palindrome.append(digit * pairs)
                count[digit] -= pairs * 2
        
        for digit in map(str, range(9, -1, -1)):
            if count[digit] > 0:
                middle_char = digit
                break

        half_palindrome_str = ''.join(half_palindrome)

        if half_palindrome_str:
            largest_palindrome = half_palindrome_str + middle_char + half_palindrome_str[::-1]
            if largest_palindrome[0] == '0': 
                return middle_char or '0'        
            return largest_palindrome
        else:
            return middle_char or '0'