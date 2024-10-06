class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 0
        apples = 0
        while apples < neededApples:
            n += 1
            apples += 12 * n * n
        return 8 * n