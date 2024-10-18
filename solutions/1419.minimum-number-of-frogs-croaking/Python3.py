class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counts = [0] * 5  # to store counts of 'c', 'r', 'o', 'a', 'k'
        croak_index = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        max_frogs = current_frogs = 0

        for char in croakOfFrogs:
            idx = croak_index[char]
            if idx == 0:
                current_frogs += 1
                max_frogs = max(max_frogs, current_frogs)
            elif counts[idx - 1] == 0:
                return -1
            if idx > 0:
                counts[idx - 1] -= 1
            counts[idx] += 1
            
            if idx == 4:
                current_frogs -= 1
                counts[4] -= 1
        
        if any(counts):
            return -1
        return max_frogs