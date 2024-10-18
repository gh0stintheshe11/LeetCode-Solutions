class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less_than = []
        equal_to = []
        greater_than = []

        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)

        return less_than + equal_to + greater_than