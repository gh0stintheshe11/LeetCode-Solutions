class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        import re
        # Replace all non-digit characters with space
        word = re.sub('[a-z]', ' ', word)
        # Split the string by spaces to extract numbers
        numbers = word.split()
        # Convert the numbers to integers to handle leading zeros and store in a set
        unique_numbers = set(int(num) for num in numbers)
        return len(unique_numbers)