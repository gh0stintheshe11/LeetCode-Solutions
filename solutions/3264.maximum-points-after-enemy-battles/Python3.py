class Solution:
    maximumPoints = lambda _, e, c: (sum(e) + c - (m := min(e))) // m * (m <= c)