class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        from collections import Counter

        # Count the frequency of each character in the string
        freq = Counter(s)
        
        # If there are fewer than k occurrences of any character, it's impossible
        if any(freq[char] < k for char in 'abc'):
            return -1
        
        total_a = freq['a']
        total_b = freq['b']
        total_c = freq['c']

        # Calculate the required number of each character from the left plus right
        required_a = total_a - k
        required_b = total_b - k
        required_c = total_c - k
        
        n = len(s)
        left_counter = Counter()
        
        # Initially consider all characters taken from the right
        minimum_minutes = n
        
        # Sliding window approach
        # Start with taking 0 characters from the left
        left = 0
        for right in range(n):
            left_counter[s[right]] += 1

            # Check if the current substring from left to right fulfills the requirement
            while (
                left_counter['a'] > required_a or
                left_counter['b'] > required_b or
                left_counter['c'] > required_c
            ):
                left_counter[s[left]] -= 1
                left += 1
            
            # Calculate the size of left + right taken characters
            current_minutes = left + (n - 1 - right)
            minimum_minutes = min(minimum_minutes, current_minutes)
        
        return minimum_minutes