from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price, and for ties by descending beauty
        items.sort()
        max_beauty = 0
        max_beauties = []
        
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            max_beauties.append((price, max_beauty))

        # Sort queries with their indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        # Prepare the result array
        result = [0] * len(queries)
        
        i = 0
        # Iterate through each query in sorted order
        for q, original_index in sorted_queries:
            # Process items up to the price that is greater than the current query
            while i < len(max_beauties) and max_beauties[i][0] <= q:
                i += 1
            
            # If i == 0, no item can satisfy the query (all items have price greater than query)
            if i > 0:
                result[original_index] = max_beauties[i - 1][1]
        
        return result