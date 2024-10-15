from typing import List

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10**9 + 7

        # Helper function to calculate factorial modulo MOD
        def factorial_mod(x):
            result = 1
            for i in range(2, x + 1):
                result = result * i % MOD
            return result

        # Helper function to calculate power of two modulo MOD
        def power_of_two_mod(exp):
            result = 1
            base = 2
            while exp > 0:
                if exp % 2 == 1:
                    result = result * base % MOD
                base = base * base % MOD
                exp //= 2
            return result
        
        # Initialize variables
        segments = []
        total_uninfected = 0
        segment_start = 0

        # Calculate segments and uninfected people
        for i in range(len(sick) - 1):
            left_bound = sick[i]
            right_bound = sick[i + 1]
            segment_length = right_bound - left_bound - 1
            if segment_length > 0:
                segments.append(segment_length)
                total_uninfected += segment_length
        
        # Handle beginning and end segments
        beginning_segment_length = sick[0]
        end_segment_length = n - 1 - sick[-1]

        # Calculate initial factorial S!
        total_factorial = factorial_mod(total_uninfected + beginning_segment_length + end_segment_length)
        
        # Calculate contribution from internal segments (2^(len(segment) - 1) * len(segment)!)
        internal_factorial = 1
        power_contribution = 0
        for segment in segments:
            internal_factorial = internal_factorial * factorial_mod(segment) % MOD
            power_contribution += segment - 1
        
        # Calculate ending pieces factor (fac(len_beginning) and fac(len_end))
        ending_factorial = factorial_mod(beginning_segment_length) * factorial_mod(end_segment_length) % MOD
        
        # Calculate result based on combinatorial logic
        result = total_factorial * power_of_two_mod(power_contribution) % MOD
        result = result * pow(internal_factorial, MOD - 2, MOD) % MOD
        result = result * pow(ending_factorial, MOD - 2, MOD) % MOD

        return result