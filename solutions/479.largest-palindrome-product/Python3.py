class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        for i in range(upper, lower - 1, -1):
            palindromic = int(str(i) + str(i)[::-1])
            for j in range(upper, lower - 1, -1):
                if j * j < palindromic:
                    break
                if palindromic % j == 0 and lower <= palindromic // j <= upper:
                    return palindromic % 1337
        return 0