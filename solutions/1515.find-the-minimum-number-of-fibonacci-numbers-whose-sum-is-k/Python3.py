class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Generate all Fibonacci numbers less than or equal to k
        fibonacci = [1, 1]
        while fibonacci[-1] <= k:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
        # Greedily find the minimum number of Fibonacci numbers that sum up to k
        count = 0
        idx = len(fibonacci) - 1
        while k > 0:
            if fibonacci[idx] <= k:
                k -= fibonacci[idx]
                count += 1
            idx -= 1
        return count