from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        max_len = 30  # Maximum length to consider as hinted
        index_map = {}
        
        # Iterate over all possible substrings of length <= 30
        for start in range(n):
            value = 0
            # Check each possible endpoint for substrings up to max_len
            for end in range(start, min(start + max_len, n)):
                value = (value << 1) | int(s[end])
                
                # If not stored, or found a shorter length, update the map
                if value not in index_map or end - start < index_map[value][1] - index_map[value][0]:
                    index_map[value] = (start, end)
        
        # Process each query
        result = []
        for first, second in queries:
            required_value = first ^ second  # val ^ firsti == secondi
            if required_value in index_map:
                result.append(list(index_map[required_value]))
            else:
                result.append([-1, -1])
        
        return result