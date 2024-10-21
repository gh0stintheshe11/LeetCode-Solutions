from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Tables to keep track where the next odd/even jump leads
        odd_next = [0] * n
        even_next = [0] * n

        # Indices sorted by the values of the array
        sorted_indices = sorted(range(n), key=lambda i: (arr[i], i))
        stack = []
        
        # Next higher jump (odd jump)
        for i in sorted_indices:
            while stack and stack[-1] < i:
                odd_next[stack.pop()] = i
            stack.append(i)
        
        # Indices sorted by the reverse values of the array
        sorted_indices = sorted(range(n), key=lambda i: (-arr[i], i))
        stack = []
        
        # Next lower jump (even jump)
        for i in sorted_indices:
            while stack and stack[-1] < i:
                even_next[stack.pop()] = i
            stack.append(i)
            
        # dp tables to check if we can reach the end from index i with odd/even jumps
        odd_reach = [False] * n
        even_reach = [False] * n
        odd_reach[-1] = even_reach[-1] = True
        
        # Traverse the array in reverse
        for i in range(n - 2, -1, -1):
            odd_reach[i] = odd_next[i] and even_reach[odd_next[i]]
            even_reach[i] = even_next[i] and odd_reach[even_next[i]]
        
        # Count the number of indices from which we can reach the end using an odd jump
        return sum(odd_reach)