class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        import itertools
        upper_bound = 2**31 - 1
        for i in range(1, 11):
            for val in sorted(int(''.join(val)) for val in itertools.product(f'{digit1}{digit2}', repeat=i)):
                if val >= upper_bound: return -1
                if val > k and not val % k: return val
        return -1