class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # If lengths are different, they can't be made equal by a single swap
        if len(s) != len(goal):
            return False
        
        # If the strings are identical, check for duplicate characters
        if s == goal:
            # Check if there is any character that appears more than once
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False
        
        # Find the positions where the characters differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        # There must be exactly two positions where they differ
        if len(diff) != 2:
            return False
        
        # Check if swapping the characters at these positions makes the strings equal
        i, j = diff
        return s[i] == goal[j] and s[j] == goal[i]
