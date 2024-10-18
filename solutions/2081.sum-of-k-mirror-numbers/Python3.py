class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(num):
            s = str(num)
            return s == s[::-1]

        def to_base(num, base):
            if num == 0:
                return '0'
            res = []
            while num:
                res.append(str(num % base))
                num //= base
            return ''.join(res[::-1])

        def generate_kmirror(length):
            if length == 1:
                for i in range(1, 10):
                    yield i
            else:
                half = (length + 1) // 2
                for i in range(10 ** (half - 1), 10 ** half):
                    left = str(i)
                    right = left[:-1] if length % 2 == 1 else left
                    yield int(left + right[::-1])

        sum_k_mirrors = 0
        count = 0
        current_length = 1

        while count < n:
            for num in generate_kmirror(current_length):
                if is_palindrome(to_base(num, k)):
                    sum_k_mirrors += num
                    count += 1
                    if count == n:
                        break
            current_length += 1

        return sum_k_mirrors