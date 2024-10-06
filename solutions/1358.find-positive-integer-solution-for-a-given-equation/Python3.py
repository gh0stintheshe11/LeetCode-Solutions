class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        x, y = 1, 1000
        
        while x <= 1000 and y > 0:
            value = customfunction.f(x, y)
            if value == z:
                result.append([x, y])
                x += 1
                y -= 1
            elif value < z:
                x += 1
            else:
                y -= 1

        return result