class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        # Using the Chicken McNugget Theorem
        return primeOne * primeTwo - primeOne - primeTwo