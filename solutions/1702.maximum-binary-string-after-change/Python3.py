class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # Count the number of leading ones
        n = len(binary)
        zero_count = one_count = 0
        found_first_zero = False
        
        for c in binary:
            if c == '0':
                if not found_first_zero:
                    found_first_zero = True
                zero_count += 1
            elif not found_first_zero:
                one_count += 1
        
        if zero_count <= 1:
            return binary  # No transformations possible; return the original

        # Creating the resultant string
        # Maximize around the first 0 that appears
        # The zeros can be shifted to be all ones with only one zero at position
        # ones before zero + number of zeros - 1 (because first zero turns to one)
        max_binary = '1' * (one_count + zero_count - 1) + '0' + '1' * (n - one_count - zero_count)
        
        return max_binary