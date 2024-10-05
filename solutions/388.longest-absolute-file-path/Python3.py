class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}  # Use a dictionary to store path lengths at each level
        
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            if '.' in name:  # It's a file
                max_len = max(max_len, path_len[depth] + len(name))
            else:  # It's a directory
                path_len[depth + 1] = path_len[depth] + len(name) + 1  # Add 1 for the "/" character
        
        return max_len