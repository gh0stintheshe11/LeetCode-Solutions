class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev_index = 0
        
        for index in spaces:
            result.append(s[prev_index:index])
            result.append(" ")
            prev_index = index
        
        result.append(s[prev_index:])  # Add the remainder of the string
        
        return ''.join(result)