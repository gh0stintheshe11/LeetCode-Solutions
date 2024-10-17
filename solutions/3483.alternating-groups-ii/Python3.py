class Solution:
    numberOfAlternatingGroups = lambda _, C, k, c=1: sum([k <= (c := c * (C[i] != C[i-1]) + 1) for i in range(-k+2, len(C))])