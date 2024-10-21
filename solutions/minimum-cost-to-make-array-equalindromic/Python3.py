class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def is_palindrome(x: int) -> bool:
            s = str(x)
            return s == s[::-1]
        
        def generate_palindrome_candidates(m: int) -> List[int]:
            s = str(m)
            n = len(s)
            candidates = set()
            
            # Create palindromes using half of the digits +1
            for i in range(n//2, n//2 + 2):
                if i > 0:
                    prefix = int(s[:i])
                    for delta in (-1, 0, 1):
                        p = str(prefix + delta)
                        # Even length palindrome
                        even_palindrome = int(p + p[::-1])
                        if even_palindrome > 0:
                            candidates.add(even_palindrome)
                        # Odd length palindrome
                        odd_palindrome = int(p + p[-2::-1])
                        candidates.add(odd_palindrome)
            return candidates

        nums.sort()
        n = len(nums)
        median = nums[n // 2]

        palindromes = generate_palindrome_candidates(median)
        
        def calculate_cost(target: int) -> int:
            return sum(abs(num - target) for num in nums)

        return min(calculate_cost(palindrome) for palindrome in palindromes if palindrome < 10**9)