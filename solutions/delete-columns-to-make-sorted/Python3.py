class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break
        return delete_count