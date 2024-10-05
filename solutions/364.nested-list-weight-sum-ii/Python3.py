from typing import List

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # Function to compute depth sum inverse
        unweighted, weighted = 0, 0
        
        while nestedList:
            next_level = []
            for ni in nestedList:
                if ni.isInteger():
                    unweighted += ni.getInteger()
                else:
                    next_level.extend(ni.getList())
            weighted += unweighted
            nestedList = next_level
        
        return weighted