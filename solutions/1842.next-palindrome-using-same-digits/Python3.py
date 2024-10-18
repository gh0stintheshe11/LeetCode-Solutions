class Solution:
    def nextPalindrome(self, num: str) -> str:
        def next_permutation(arr):
            # Find the first element which is smaller than the next
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return False
            # Find the element just larger than arr[i] from the right
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
            # Reverse the sequence from i + 1 to the end
            arr[i + 1:] = arr[i + 1:][::-1]
            return True
        
        n = len(num)
        if n <= 1:
            return ""
        
        half = num[:n//2]
        half_list = list(half)
        
        if not next_permutation(half_list):
            return ""
        
        next_half = ''.join(half_list)
        
        if n % 2 == 0:
            return next_half + next_half[::-1]
        else:
            return next_half + num[n//2] + next_half[::-1]