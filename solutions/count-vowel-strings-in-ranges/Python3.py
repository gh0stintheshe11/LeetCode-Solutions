from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Compute a prefix sum for vowel strings
        prefix_sum = [0] * (len(words) + 1)
        
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum[i+1] = prefix_sum[i] + 1
            else:
                prefix_sum[i+1] = prefix_sum[i]
        
        # Process each query using the prefix sum
        result = []
        for li, ri in queries:
            result.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return result