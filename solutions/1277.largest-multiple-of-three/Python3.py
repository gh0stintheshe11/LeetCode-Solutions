from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        
        remainder_buckets = [[], [], []]
        total_sum = 0
        
        for digit in digits:
            total_sum += digit
            remainder_buckets[digit % 3].append(digit)
        
        remainder = total_sum % 3
        
        if remainder != 0:
            if remainder_buckets[remainder]:
                remainder_buckets[remainder].pop()
            else:
                to_remove = 2 if remainder == 1 else 1  # if remainder == 1, we need to remove 2 lowest numbers of remainder 2
                if len(remainder_buckets[to_remove]) >= 2:
                    remainder_buckets[to_remove].pop()
                    remainder_buckets[to_remove].pop()
                else:
                    return ""
        
        result = remainder_buckets[0] + remainder_buckets[1] + remainder_buckets[2]
        result.sort(reverse=True)
        
        if result and result[0] == 0:
            return "0"  # All numbers are zero
        return "".join(map(str, result))