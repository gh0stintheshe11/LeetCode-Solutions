from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            suggestions = []
            start = self.binarySearch(products, prefix)

            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break

            result.append(suggestions)

        return result

    def binarySearch(self, products: List[str], prefix: str) -> int:
        left, right = 0, len(products)

        while left < right:
            mid = (left + right) // 2
            if products[mid] < prefix:
                left = mid + 1
            else:
                right = mid

        return left