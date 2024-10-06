class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Calculate the rightmost 1 for each row
        rightmost_one = []
        for row in grid:
            rightmost = -1
            for j in range(n-1, -1, -1):
                if row[j] == 1:
                    rightmost = j
                    break
            rightmost_one.append(rightmost)
        
        swaps = 0
        for i in range(n):
            # We need the rightmost one to be at most position i
            if rightmost_one[i] <= i:
                continue
            found = False
            # Find the row with rightmost 1 <= i
            for j in range(i+1, n):
                if rightmost_one[j] <= i:
                    # Swap rows until this row is in position i
                    found = True
                    for k in range(j, i, -1):
                        rightmost_one[k], rightmost_one[k-1] = rightmost_one[k-1], rightmost_one[k]
                        swaps += 1
                    break
            if not found:
                return -1
            
        return swaps