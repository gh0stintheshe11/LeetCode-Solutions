class Solution:
    def toLowerCase(self, s: str) -> str:
        # Initialize an empty list to store the result characters
        result = []
        
        # Iterate through each character in the input string
        for char in s:
            # Check if the character is an uppercase letter
            if 'A' <= char <= 'Z':
                # Convert the uppercase letter to lowercase by adding 32 to its ASCII value
                lower_char = chr(ord(char) + 32)
                result.append(lower_char)
            else:
                # If the character is not an uppercase letter, keep it as is
                result.append(char)
        
        # Join the list of characters into a single string and return it
        return ''.join(result)