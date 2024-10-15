class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_valid(start, first, second):
            while start < len(num):
                third = first + second
                third_str = str(third)
                if not num.startswith(third_str, start):
                    return False
                start += len(third_str)
                first, second = second, third
            return True

        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                first, second = num[:i], num[i:j]
                if (first.startswith('0') and len(first) > 1) or (second.startswith('0') and len(second) > 1):
                    continue
                if is_valid(j, int(first), int(second)):
                    return True
        return False