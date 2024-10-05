class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_unique_digit_numbers(m):
            digits = list(map(int, str(m + 1)))
            nDigits = len(digits)
            all_unique = 0
            
            # Step 1: count numbers with length < nDigits
            for length in range(1, nDigits):
                all_unique += 9 * perm(9, length - 1)
                
            # Step 2: count numbers with the same length but restricted by prefix
            seen = set()
            for i in range(nDigits):
                for x in range(1 if i == 0 else 0, digits[i]):
                    if x in seen:
                        continue
                    all_unique += perm(9 - i, nDigits - i - 1)
                if digits[i] in seen:
                    break
                seen.add(digits[i])
                
            return all_unique

        def perm(m, n):
            if n == 0:
                return 1
            return perm(m, n - 1) * (m - (n - 1))

        return n - count_unique_digit_numbers(n)