class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        
        # Define the frequency requirement for each character in "balloon"
        balloon_count = Counter('balloon')
        
        # Count the occurrences of each character in the input text
        text_count = Counter(text)
        
        # Determine minimum number of times "balloon" can be formed
        return min(text_count[char] // balloon_count[char] for char in balloon_count)