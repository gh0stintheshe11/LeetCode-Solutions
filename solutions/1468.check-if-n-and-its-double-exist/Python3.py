class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        value_set = set()
        for num in arr:
            if 2 * num in value_set or (num % 2 == 0 and num // 2 in value_set):
                return True
            value_set.add(num)
        return False