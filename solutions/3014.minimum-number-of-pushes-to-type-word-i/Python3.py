class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        # We can have 8 keys, hence 26 letters will be equally divided across them
        pushes = 0
        characters_per_push = 1
        
        i = 0
        while i < length:
            # Calculate number of letters that can be typed with current push count
            letters_to_type = min(8, length - i)
            pushes += letters_to_type * characters_per_push
            characters_per_push += 1
            i += letters_to_type
        
        return pushes