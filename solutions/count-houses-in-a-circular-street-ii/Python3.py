class Solution:
    def houseCount(self, S, K, i=0, A=0):
        while not S.isDoorOpen():
            S.moveRight()
        while i < K:
            S.moveRight()
            i += 1
            if S.isDoorOpen():
                S.closeDoor()
                A = i
        return A