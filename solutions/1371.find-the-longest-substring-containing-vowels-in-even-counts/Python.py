class Solution:
    def findTheLongestSubstring(self, s):
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state_to_index = {0: -1}  # Initial state before starting
        state = 0
        max_length = 0

        for i, c in enumerate(s):
            if c in vowel_to_bit:
                # Flip the corresponding bit for the vowel
                state ^= (1 << vowel_to_bit[c])

            # If the state has been seen before, update max_length
            if state in state_to_index:
                prev_index = state_to_index[state]
                max_length = max(max_length, i - prev_index)
            else:
                # Record the first occurrence of this state
                state_to_index[state] = i

        return max_length


