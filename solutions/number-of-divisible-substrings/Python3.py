from collections import defaultdict 
class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        
        def count_divisible_for_digit(try_digit, mapped_digits):
            seen = defaultdict(int)
            seen[0] = 1
            sub_count = prefix_sum =  0
            for mapped_digit in mapped_digits:
                prefix_sum += mapped_digit - try_digit
                sub_count += seen[prefix_sum]
                seen[prefix_sum] += 1
            return sub_count

        mapped_digits = [(ord(char) - ord('c')) // 3 +  2 
                         for char in word]

        return sum(
                    count_divisible_for_digit(try_digit, mapped_digits) 
                    for try_digit in range(1, 10)
                )