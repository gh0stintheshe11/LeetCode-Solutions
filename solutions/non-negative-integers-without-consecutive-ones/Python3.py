class Solution:
    def findIntegers(self, n: int) -> int:
        # Convert n to binary representation in string form
        binary = bin(n)[2:]
        length = len(binary)

        # Initialize arrays for Fibonacci sequence
        fib = [0] * (length + 1)
        fib[0], fib[1] = 1, 2

        for i in range(2, length + 1):
            fib[i] = fib[i - 1] + fib[i - 2]

        result, last_bit = 0, 0

        for i in range(length):
            if binary[i] == '1':
                result += fib[length - i - 1]
                if last_bit == 1:
                    return result
                last_bit = 1
            else:
                last_bit = 0

        return result + 1