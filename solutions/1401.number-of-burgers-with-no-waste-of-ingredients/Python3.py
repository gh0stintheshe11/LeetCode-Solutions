class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # Check if the number of tomato slices is even and if the number of cheese slices is suitable
        if tomatoSlices % 2 != 0 or cheeseSlices * 2 > tomatoSlices or cheeseSlices * 4 < tomatoSlices:
            return []
        
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo
        return [jumbo, small]