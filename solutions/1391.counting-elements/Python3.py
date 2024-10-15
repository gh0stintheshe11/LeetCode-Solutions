class Solution:
    def countElements(self, arr: List[int]) -> int:
        element_set = set(arr)
        count = 0
        for x in arr:
            if x + 1 in element_set:
                count += 1
        return count