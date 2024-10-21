class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            total = 0
            for ni in nestedList:
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    total += dfs(ni.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)