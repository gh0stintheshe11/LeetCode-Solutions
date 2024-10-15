class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        current_number = 1
        for num in target:
            while current_number < num:
                operations.append("Push")
                operations.append("Pop")
                current_number += 1
            operations.append("Push")
            current_number += 1
        return operations