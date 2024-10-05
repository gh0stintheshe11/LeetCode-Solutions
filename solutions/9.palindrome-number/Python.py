class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        s_rev = s[::-1]
        for i, n in enumerate(s_rev):
            if n is not s[i]:
                return False
        return True
        