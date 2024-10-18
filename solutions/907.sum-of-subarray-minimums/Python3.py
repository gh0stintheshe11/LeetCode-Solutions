class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        # Initialize variables
        stack = []
        answer = 0
        n = len(arr)

        # Next Smaller Element array
        nse = [n] * n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                nse[stack.pop()] = i
            stack.append(i)

        # Previous Smaller Element array
        stack = []
        pse = [-1] * n

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        # Calculate the sum of subarray minimums
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            answer = (answer + arr[i] * left * right) % MOD
        
        return answer