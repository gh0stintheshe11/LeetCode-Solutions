class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        evenXCount = n // 2
        oddXCount = n - evenXCount
        evenYCount = m // 2
        oddYCount = m - evenYCount
        
        # Alice wins if x and y have different parities
        # Possible pairs where x is odd and y is even
        oddX_evenY_Pairs = oddXCount * evenYCount
        
        # Possible pairs where x is even and y is odd
        evenX_oddY_Pairs = evenXCount * oddYCount

        return oddX_evenY_Pairs + evenX_oddY_Pairs