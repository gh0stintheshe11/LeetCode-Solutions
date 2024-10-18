class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        count = []
        
        for i in range(sideLength):
            for j in range(sideLength):
                count.append(((width - i - 1) // sideLength + 1) * ((height - j - 1) // sideLength + 1))
        
        count.sort(reverse=True)
        
        return sum(count[:maxOnes])