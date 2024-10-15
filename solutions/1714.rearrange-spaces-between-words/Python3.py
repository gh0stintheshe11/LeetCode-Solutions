class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Split the text by spaces to get the words, ignoring empty parts
        words = text.split()
        
        # Count total spaces
        total_spaces = text.count(' ')
        
        # Number of words
        number_of_words = len(words)
        
        if number_of_words == 1:
            # If there's only one word, all spaces go after it
            return words[0] + ' ' * total_spaces
        
        # Calculate spaces to distribute between words and extra spaces
        spaces_between_words = total_spaces // (number_of_words - 1)
        extra_spaces = total_spaces % (number_of_words - 1)
        
        # Join words with calculated spaces in between and add extra spaces at the end
        return (' ' * spaces_between_words).join(words) + ' ' * extra_spaces