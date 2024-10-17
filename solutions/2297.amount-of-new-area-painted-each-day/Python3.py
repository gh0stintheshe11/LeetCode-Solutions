from typing import List

class Painted:
    def __init__(self):
        self.paintedAreas = []
        self.combinedSegs = []

    def insert(self, s: int, e: int):
        if len(self.paintedAreas) < 1:
            self.paintedAreas.append(e-s)
            self.combinedSegs.append([s, e])
            return
        tempResult = []
        remainderQue = deque()
        remainderQue.append([s, e])
        while remainderQue:
            remainder = remainderQue.popleft()
            for idx in range(len(self.combinedSegs)-1, -1, -1):
                cur = self.combinedSegs[idx]
                if self.isOverlap(remainder[0], remainder[1], cur[0], cur[1]):
                    remainderPool = self.subtract(
                        remainder[0], remainder[1], 
                        cur[0], cur[1]
                    )
                    remainder = remainderPool[0]
                    if len(remainderPool) == 2:
                        remainderQue.append(remainderPool[1])
                    if remainder[1]-remainder[0] == 0:
                        break
            tempResult.append(remainder)
        
        area = 0
        for seg in tempResult:
            area += seg[1] - seg[0]
        self.paintedAreas.append(area)

        while tempResult:
            curSeg = tempResult.pop()
            isUnioned = False
            for idx in range(len(self.combinedSegs)-1, -1, -1):
                prvSeg = self.combinedSegs[idx]
                newSeg = self.union(curSeg[0], curSeg[1], prvSeg[0], prvSeg[1])
                if newSeg:
                    isUnioned = True
                    self.combinedSegs[idx] = newSeg
            if not isUnioned:
                self.combinedSegs.append(curSeg)

    def isOverlap(self, s1, e1, s2, e2, forUnion=False):
        if forUnion and s1 <= e2 and e1 >= s2:
            return True
        if s1 < e2 and e1 > s2:
            return True
        return False
    
    def union(self, s1, e1, s2, e2) -> List[int]:
        if not self.isOverlap(s1, e1, s2, e2, forUnion=True):
            return None
        S = min(s1, s2, e1, e2)
        E = max(s1, s2, e1, e2)
        return [S, E]

    def subtract(self, s1, e1, s2, e2):
        if not self.isOverlap(s1, e1, s2, e2):
            None
        if s1 == s2 and e1 == e2:
            return [[s1, s1]]
        elif s1 == s2 and e2 > e1:
            return [[s1, s1]]
        elif e1 == e2 and s2 < s1:
            return [[e1, e1]]
        elif s1 > s2 and e1 < e2:
            return [[s1, s1]]
        elif s1 < s2 and e1 > e2:
            return [[s1, s2], [e2, e1]]
        else:
            if s1 < s2:
                S = s1
                E = s2
            else:  
                S = e2
                E = e1
            return [[S, E]]
        
    def getTotal(self):
        return self.paintedAreas


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        counter = Painted()
        for idx in range(len(paint)):
            seg = paint[idx]
            counter.insert(seg[0], seg[1]) 
        return counter.getTotal()