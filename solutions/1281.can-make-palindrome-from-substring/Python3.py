from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        # Create a prefix sum array for character counts
        # There are 26 lowercase English letters, use a bitmask to track odd/even status
        prefix = [0] * (n + 1) 
        
        for i in range(n):
            # Set the corresponding bit for the current character
            # Toggle the bit using XOR operation
            prefix[i + 1] = prefix[i] ^ (1 << (ord(s[i]) - ord('a')))
        
        res = []
        
        for left, right, k in queries:
            # Calculate bitmask for the substring
            odd_count = bin(prefix[right + 1] ^ prefix[left]).count('1')
            # Check if the number of transformations (k) can accommodate half the odd characters
            res.append(odd_count // 2 <= k)
        
        return res