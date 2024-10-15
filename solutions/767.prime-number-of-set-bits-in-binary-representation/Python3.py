class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            if n in (2, 3):
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        prime_count_bits = {i for i in range(21) if is_prime(i)}
        
        def count_set_bits(num):
            return bin(num).count('1')

        count = 0
        for num in range(left, right + 1):
            if count_set_bits(num) in prime_count_bits:
                count += 1
                
        return count