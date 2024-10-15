class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        
        # Calculate total XOR of all numbers from 1 to n
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i
        
        # Calculate XOR of all elements at odd indices in encoded
        encoded_odd_xor = 0
        for i in range(1, len(encoded), 2):
            encoded_odd_xor ^= encoded[i]
        
        # Calculate first element of the perm array
        perm0 = total_xor ^ encoded_odd_xor
        
        # Decode the entire perm array using the first element
        perm = [0] * n
        perm[0] = perm0
        for i in range(1, n):
            perm[i] = perm[i - 1] ^ encoded[i - 1]
        
        return perm