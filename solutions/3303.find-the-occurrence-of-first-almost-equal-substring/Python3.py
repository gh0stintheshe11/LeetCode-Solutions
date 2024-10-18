class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        full_overlaps = len(s)-len(pattern)+1
        fwd_z = get_z(s, pattern)[:full_overlaps]
        bwd_z = get_z(s[::-1], pattern[::-1])[:full_overlaps]

        for i, (fwd_match, bwd_match) in enumerate(zip(fwd_z, reversed(bwd_z))):
            if fwd_match + bwd_match >= len(pattern) - 1:
                return i
        
        return -1

def get_z(s, pattern):
    full_s = pattern + "#" + s
    full_z = calculate_z(full_s)
    return full_z[len(pattern) + 1:]

def calculate_z(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0  # Z-box
    
    for i in range(1, n):

        # Case 1: i is outside the current Z-box
        if i > r:
            match_length = 0
            while i + match_length < n and s[i + match_length] == s[match_length]:
                match_length += 1
            
            l = i
            r = i + match_length - 1
            z[i] = match_length

        # Case 2: i is inside the current Z-box
        else:
            index_within_box = i - l
            remaining_values = r - i + 1

            # Case 2a: Value does not stretch outside the Z-box
            if z[index_within_box] < remaining_values:
                z[i] = z[index_within_box]

            # Case 2b: Value stretches outside the Z-box
            else:
                match_length = remaining_values
                while i + match_length < n and s[i + match_length] == s[match_length]:
                    match_length += 1
                    
                l = i
                r = i + match_length - 1
                z[i] = match_length
    return z