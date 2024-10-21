class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        from itertools import product
        
        # Reduce each row to unique sorted list
        mat = [sorted(set(row)) for row in mat]
        
        # Initialize a set with the possible sums for the first row
        possible_sums = set(mat[0])
        
        # Iterate through each row starting from the second one
        for row in mat[1:]:
            new_sums = set()
            for a in possible_sums:
                for b in row:
                    new_sums.add(a + b)
            possible_sums = new_sums
        
        # Find the minimum absolute difference
        return min(abs(s - target) for s in possible_sums)