class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        c = 0
        prefix_count = 0
        # Calculate the number of digits in the k-th lucky number
        while k > prefix_count:
            c += 1
            prefix_count += 2 ** c
        
        # Roll back to the previous level
        prefix_count -= 2 ** c
        # Determine the position within numbers of c digits
        position = k - prefix_count - 1
        # Convert position to binary and map 0 to '4' and 1 to '7'
        binary_representation = bin(position)[2:].zfill(c)
        return ''.join('4' if x == '0' else '7' for x in binary_representation)