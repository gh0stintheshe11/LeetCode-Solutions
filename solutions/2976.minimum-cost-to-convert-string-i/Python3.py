from typing import List
import sys

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Number of alphabet letters
        ALPHABET_SIZE = 26
        
        # Initialize cost matrix with large values
        inf = sys.maxsize
        change_cost = [[inf] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]

        # This function returns the index of a character a-z
        def char_index(c):
            return ord(c) - ord('a')

        # Initialize direct change costs
        for i in range(len(original)):
            o_idx = char_index(original[i])
            c_idx = char_index(changed[i])
            change_cost[o_idx][c_idx] = min(change_cost[o_idx][c_idx], cost[i])
        
        # Floyd-Warshall algorithm to compute the minimum cost of conversion between every pair of characters
        for k in range(ALPHABET_SIZE):
            for i in range(ALPHABET_SIZE):
                for j in range(ALPHABET_SIZE):
                    if change_cost[i][k] < inf and change_cost[k][j] < inf:
                        change_cost[i][j] = min(change_cost[i][j], change_cost[i][k] + change_cost[k][j])
        
        total_cost = 0

        # Calculate the total cost to convert the source to target
        for s_c, t_c in zip(source, target):
            if s_c == t_c:
                continue
            s_idx = char_index(s_c)
            t_idx = char_index(t_c)
            min_cost = change_cost[s_idx][t_idx]
            
            if min_cost >= inf:
                return -1
                
            total_cost += min_cost

        return total_cost