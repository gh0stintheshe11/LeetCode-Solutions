import sys 
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        sys.set_int_max_str_digits(20000000)
        p = 1
        for i in range(left, right+1):
            p *= i
        s = str(p)
        c = len(s) 
        s = s.rstrip('0')
        c = c - len(s)
        if len(s) > 10:
            return '%s...%se%s' % (s[:5], s[-5:], str(c))
        return '%se%s' % (s, str(c))