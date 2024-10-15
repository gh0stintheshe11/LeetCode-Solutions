class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank > 0:
            if mainTank >= 5 and additionalTank > 0:
                distance += 50
                mainTank -= 4
                additionalTank -= 1
            else:
                distance += mainTank * 10
                break
        return distance